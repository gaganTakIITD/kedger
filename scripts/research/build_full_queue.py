#!/usr/bin/env python3
"""Build Kedger Track 0 FULL deep-read queue (≥500 slots).

Scans research/docs markdown for arXiv-like IDs, loads FULL ledger rows from
CORPUS_INVENTORY.md, prioritizes remaining items into tiers 1–6, and pads with
honest survey-seed placeholders when unique IDs are below 500.

Does NOT mark unread papers as FULL.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
RESEARCH = DOCS / "research"
INVENTORY = RESEARCH / "CORPUS_INVENTORY.md"
OUT_MD = RESEARCH / "queue" / "FULL_QUEUE_500.md"
OUT_JSONL = RESEARCH / "queue" / "full_queue.jsonl"

# YYMM.NNNNN (4–5 digit paper number); strip optional version suffix on match.
ARXIV_RE = re.compile(r"(?<![0-9./])(\d{4}\.\d{4,5})(?:v\d+)?(?![0-9])")

TIER_LABELS = {
    1: "eval/failure",
    2: "capture/compaction",
    3: "episode/boundary",
    4: "graph/conflict",
    5: "privacy/capability",
    6: "eng-judgment",
}

# Keyword → priority tier (first match wins; lower number = higher priority).
TIER_RULES: list[tuple[int, re.Pattern[str]]] = [
    (
        1,
        re.compile(
            r"eval|bench|locomo|longmemeval|memoryagentbench|memorybench|dialsim|"
            r"confaide|failure|leakage.?probe|judge|realmem|membench|memoryarena|"
            r"lost.in.the.middle|"
            r"agentbench|gaia|webarena|crag|multihop.?rag|hotpot|2wiki|"
            r"freshqa|freshllm|perltqa|needlebench|ruler|longbench|"
            r"∞bench|infinitebench|self.?rag|rgb|corrective.?retrieval|"
            r"adaptive.?chameleon|knowledge.?conflict|conflictqa",
            re.I,
        ),
    ),
    (
        2,
        re.compile(
            r"capture|compact|kv|streamingllm|snapkv|h.?o|landmark|memgpt|hook|"
            r"working.?state|pressure|evict|compressive|transformer-xl|rmt|"
            r"autocompressor|unlimiformer|icae|aios|ret-llm|context.edit",
            re.I,
        ),
    ),
    (
        3,
        re.compile(
            r"episode|boundary|cognify|segment|nemori|es-mem|recmem|est\b|"
            r"chapter|surprise|recurrence|memoryos|scm|think-in-memory|"
            r"memorybank|hema|cognitive.weave|topic.seg|voyager|larimar|"
            r"sleep.?consolidat|memobox|membox",
            re.I,
        ),
    ),
    (
        4,
        re.compile(
            r"graph|conflict|compose|hipporag|graphiti|zep|graphrag|lightrag|"
            r"arigraph|hypergraph|ssgm|statefuse|toki|supersed|entity|"
            r"ppr|openie|magma|g-memory|associat|relik|mem0",
            re.I,
        ),
    ),
    (
        5,
        re.compile(
            r"privacy|capability|seal|memclaw|agentleak|memleak|prism|fides|"
            r"camel|vault|ocap|macaroon|biscuit|age\.md|libsodium|wormhole|"
            r"mls|spki|shareable|govern|ifc|mama",
            re.I,
        ),
    ),
]

P_STAGE_RE = re.compile(r"\bP([1-6])\b")
STAGE_NAMES = {
    1: "capture_working",
    2: "episode_cognify",
    3: "anchors_graph",
    4: "conflict_compose",
    5: "hydrate_retrieve",
    6: "privacy_seal",
}


@dataclass
class QueueEntry:
    id: str
    title_hint: str
    status: str  # FULL | queued | seed_placeholder
    priority_tier: int
    kedger_stages: list[str] = field(default_factory=list)
    metric_impact: str = ""
    refine_candidate: bool = False
    source_note: str = ""


def iter_markdown_sources() -> list[Path]:
    paths: list[Path] = []
    if RESEARCH.is_dir():
        paths.extend(sorted(RESEARCH.rglob("*.md")))
    paths.extend(sorted(DOCS.glob("*.md")))
    # De-dupe while preserving order
    seen: set[Path] = set()
    out: list[Path] = []
    for p in paths:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        out.append(p)
    return out


def scan_arxiv_ids(paths: list[Path]) -> dict[str, str]:
    """Return id → best title_hint from nearby markdown table cells / mentions."""
    hints: dict[str, str] = {}
    # Table row: | ID | Title | ...
    table_row = re.compile(
        r"\|\s*([0-9]{4}\.[0-9]{4,5})(?:\s*/\s*[0-9]{4}\.[0-9]{4,5})*\s*\|\s*([^|]+)\|",
    )
    prose = re.compile(
        r"(?:arXiv:)?([0-9]{4}\.[0-9]{4,5})(?:v\d+)?\s*[—–:-]\s*([^\n|]{3,80})",
        re.I,
    )
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in ARXIV_RE.finditer(text):
            pid = m.group(1)
            hints.setdefault(pid, "")
        for m in table_row.finditer(text):
            pid = m.group(1)
            title = m.group(2).strip()
            if title and (not hints.get(pid) or len(title) > len(hints[pid])):
                hints[pid] = title
            # Also capture slash-joined IDs in classical table
            for extra in ARXIV_RE.findall(m.group(0)):
                hints.setdefault(extra, title)
        for m in prose.finditer(text):
            pid = m.group(1)
            title = m.group(2).strip(" .;")
            if title and not hints.get(pid):
                hints[pid] = title
    return hints


def load_full_from_inventory(text: str) -> dict[str, dict]:
    """Parse CORPUS_INVENTORY §2 FULL ledger tables.

    Returns id → {title, memo, stages}.
    """
    full: dict[str, dict] = {}
    in_full = False
    for line in text.splitlines():
        if line.startswith("## 2. FULL"):
            in_full = True
            continue
        if in_full and re.match(r"^## [0-9]+\.", line):
            break
        if not in_full or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells:
            continue
        first = cells[0]
        # Skip headers / separators
        if first in {"ID", "Source", "----", "--------"} or set(first) <= {"-"}:
            continue
        ids = ARXIV_RE.findall(first)
        title = cells[1] if len(cells) > 1 else first
        memo = cells[-1] if len(cells) > 2 else ""
        # Crypto/hooks table uses Source | Depth | Memo — Depth is not a title.
        if title.lower() in {"full", "substantial", "depth"}:
            title = first
            memo = cells[2] if len(cells) > 2 else memo
        stages = guess_stages(f"{title} {memo}")
        if ids:
            for pid in ids:
                full[pid] = {"title": title, "memo": memo, "stages": stages}
            continue
        # Non-arXiv FULL rows (hooks, RFCs, crypto specs, etc.)
        slug = slugify_non_arxiv(first, title)
        if slug:
            full[slug] = {"title": title if title != first else first, "memo": memo, "stages": stages}
    return full


def slugify_non_arxiv(first: str, title: str) -> str | None:
    raw = first if first not in {"—", "-", "–"} else title
    raw = raw.strip()
    if not raw or raw.lower() in {"id", "source", "note"}:
        return None
    s = raw.lower()
    s = re.sub(r"[`\"'()]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    if not s or len(s) < 3:
        return None
    if s.startswith("arxiv"):
        return None
    return s[:80]


def guess_stages(blob: str) -> list[str]:
    stages: list[str] = []
    for n in P_STAGE_RE.findall(blob):
        name = STAGE_NAMES[int(n)]
        if name not in stages:
            stages.append(name)
    # Soft keyword fallbacks when no P# present
    if not stages:
        tier = assign_tier(blob)
        fallback = {
            1: ["hydrate_retrieve"],
            2: ["capture_working"],
            3: ["episode_cognify"],
            4: ["anchors_graph", "conflict_compose"],
            5: ["privacy_seal"],
            6: ["hydrate_retrieve"],
        }
        stages = list(fallback[tier])
    return stages


def assign_tier(blob: str) -> int:
    for tier, pat in TIER_RULES:
        if pat.search(blob):
            return tier
    return 6


def metric_impact_for(tier: int, status: str) -> str:
    if status == "FULL":
        return "already_extracted"
    return {
        1: "eval_harness_or_failure_mode",
        2: "capture_budget_compaction",
        3: "episode_boundary_cognify",
        4: "graph_conflict_compose",
        5: "privacy_capability_seal",
        6: "eng_judgment_supporting",
    }[tier]


def is_refine_candidate(tier: int, status: str, blob: str) -> bool:
    if status == "FULL":
        return bool(re.search(r"eval|bench|conflict|privacy|leak|boundary|compact", blob, re.I))
    return tier in {1, 2, 3, 4, 5}


# Named sources drawn from CORPUS_INVENTORY §4 + survey bibliographies cited there
# (2512.13564, 2603.07670, 2602.05665, 2309.07864) and deep-read citation maps.
# These are NOT claimed as FULL — they pad the runway as seed_placeholder.
SURVEY_SEED_SOURCES: list[tuple[str, int, list[str]]] = [
    # (title_hint, priority_tier, kedger_stages)
    ("CaMeL — capability-based information flow control for LLMs", 5, ["privacy_seal"]),
    ("Cognee — queryable graph embeddings memory toolkit", 4, ["anchors_graph"]),
    ("OpenMemory — graph memory toolkit", 4, ["anchors_graph"]),
    ("MemMachine — graph memory toolkit", 4, ["anchors_graph"]),
    ("Memary — graph memory toolkit", 4, ["anchors_graph"]),
    ("MemoryArena — agent memory evaluation suite", 1, ["hydrate_retrieve"]),
    ("MemBench — memory benchmark suite", 1, ["hydrate_retrieve"]),
    ("RealMem — realistic memory evaluation", 1, ["hydrate_retrieve"]),
    ("FLEX — semantic gating for trajectory merge", 3, ["episode_cognify"]),
    ("Classic REBEL — seq2seq relation extraction", 4, ["anchors_graph"]),
    ("Stanford OpenIE — open information extraction", 4, ["anchors_graph"]),
    ("MemU — product memory system (survey-named)", 6, ["capture_working"]),
    ("Memobase — product memory system (survey-named)", 6, ["capture_working"]),
    ("Memento 2 (2512.22716 follow-on) — stateful reflective memory", 3, ["episode_cognify"]),
    ("LongMemEval-V2 (2605.12493) — eng-colleague eval follow-on", 1, ["hydrate_retrieve"]),
    ("DNC — Differentiable Neural Computer", 6, ["capture_working"]),
    ("AgentGit — git-like rollback/branch for agent workflows", 4, ["conflict_compose"]),
    ("Retroformer — parametric memory adaptation", 6, ["capture_working"]),
    ("Early Experience — parametric/experiential adaptation", 6, ["episode_cognify"]),
    ("MemoryLLM — latent parametric memory", 6, ["capture_working"]),
    ("M+ memory model — latent/parametric lineage", 6, ["capture_working"]),
    ("MemGen — generative parametric memory", 6, ["capture_working"]),
    ("HiAgent — working-memory manager for multi-turn tasks", 2, ["capture_working"]),
    ("ReSum — working-memory / resume manager", 2, ["capture_working"]),
    ("H2R — self-evolving memory line (survey-cited)", 3, ["episode_cognify"]),
    ("MIRIX — multi-agent memory organization (survey/toolkit)", 4, ["anchors_graph", "privacy_seal"]),
    ("Letta (MemGPT product line) docs — paging UX", 2, ["capture_working"]),
    ("Claude Code memory / CLAUDE.md patterns (docs)", 2, ["capture_working"]),
    ("Cursor Memories / Rules docs", 2, ["capture_working"]),
    ("LangGraph long-term memory store docs", 4, ["anchors_graph"]),
    ("LlamaIndex memory modules docs", 4, ["anchors_graph", "hydrate_retrieve"]),
    ("Haystack memory / agent memory docs", 6, ["hydrate_retrieve"]),
    ("CrewAI memory docs", 6, ["anchors_graph"]),
    ("AutoGPT memory backend docs", 6, ["capture_working"]),
    ("BabyAGI / task memory lineage", 6, ["episode_cognify"]),
    ("ChatDB — database-as-memory agents", 4, ["anchors_graph"]),
    ("DB-GPT memory / knowledge layer", 4, ["anchors_graph"]),
    ("ThinkGPT — thinking + memory patterns", 6, ["episode_cognify"]),
    ("ExpeL — experiential learning memory", 3, ["episode_cognify"]),
    ("ClinicalAgent / MedAgents memory slices", 6, ["privacy_seal"]),
    ("JARVIS / HuggingGPT tool memory", 2, ["capture_working"]),
    ("AppWorld / environment memory benchmarks", 1, ["hydrate_retrieve"]),
    ("AgentBench — agent evaluation harness", 1, ["hydrate_retrieve"]),
    ("GAIA benchmark — tool-use failure modes", 1, ["hydrate_retrieve"]),
    ("WebArena / BrowserGym memory carryover", 1, ["hydrate_retrieve"]),
    ("SWE-bench agent trajectory memory notes", 1, ["hydrate_retrieve"]),
    ("τ-bench / tool-agent eval memory slices", 1, ["hydrate_retrieve"]),
    ("ToolBench memory-of-tools patterns", 2, ["capture_working"]),
    ("API-Bank tool trajectory memory", 2, ["capture_working"]),
    ("RestGPT stateful API memory", 2, ["capture_working"]),
    ("OpenAgents memory modules", 6, ["anchors_graph"]),
    ("XAgent long-horizon memory", 3, ["episode_cognify"]),
    ("ChatArena multi-agent memory", 4, ["conflict_compose"]),
    ("AgentVerse multi-agent memory", 4, ["conflict_compose"]),
    ("ProAgent procedural memory", 3, ["episode_cognify"]),
    ("TPTU tool planning memory", 2, ["capture_working"]),
    ("Chameleon LLM tool composer memory", 2, ["capture_working"]),
    ("MMAC / multi-modal agent memory survey tails", 6, ["hydrate_retrieve"]),
    ("VideoAgent episodic memory", 3, ["episode_cognify"]),
    ("Cradle agent memory (game/env)", 3, ["episode_cognify"]),
    ("OdysseyAgent long-horizon memory", 3, ["episode_cognify"]),
    ("LLaMA-Rider / game skill memory", 3, ["episode_cognify"]),
    ("GITM — generally better Minecraft agents memory", 3, ["episode_cognify"]),
    ("Plan-and-Solve / plan memory", 6, ["episode_cognify"]),
    ("ReWOO planner memory separation", 2, ["capture_working"]),
    ("PEARL planning memory", 6, ["episode_cognify"]),
    ("RET-LLM follow-ons / SQL memory agents", 2, ["capture_working"]),
    ("ChatDB SQL memory (survey-cited)", 4, ["anchors_graph"]),
    ("SQL-of-Thought / NL2SQL memory", 6, ["hydrate_retrieve"]),
    ("Zep Cloud product docs (beyond paper)", 4, ["anchors_graph", "conflict_compose"]),
    ("Graphiti OSS README / temporal ops", 4, ["anchors_graph", "conflict_compose"]),
    ("Mem0 product docs / graph mode", 4, ["anchors_graph", "conflict_compose"]),
    ("HippoRAG code release / OpenIE pipeline notes", 4, ["anchors_graph"]),
    ("Microsoft GraphRAG docs / Leiden communities", 4, ["anchors_graph", "hydrate_retrieve"]),
    ("LightRAG repo docs", 4, ["anchors_graph", "hydrate_retrieve"]),
    ("Nano-GraphRAG / community variants", 4, ["anchors_graph"]),
    ("FastGraphRAG variants", 4, ["anchors_graph"]),
    ("KG-RAG / KG-enhanced RAG surveys tails", 4, ["anchors_graph", "hydrate_retrieve"]),
    ("ToG — Think-on-Graph", 4, ["anchors_graph", "hydrate_retrieve"]),
    ("StructGPT structured knowledge memory", 4, ["anchors_graph"]),
    ("Unify GraphRAG evaluation protocols", 1, ["hydrate_retrieve"]),
    ("RGB — retrieval-augmented generation benchmark", 1, ["hydrate_retrieve"]),
    ("CRAG — Corrective RAG benchmark", 1, ["hydrate_retrieve"]),
    ("MultiHop-RAG benchmark", 1, ["hydrate_retrieve"]),
    ("HotpotQA as memory multi-hop probe", 1, ["hydrate_retrieve"]),
    ("2WikiMultiHopQA probe", 1, ["hydrate_retrieve"]),
    ("MuSiQue multi-hop probe", 1, ["hydrate_retrieve"]),
    ("Bamboogle / Compose multi-hop", 1, ["hydrate_retrieve"]),
    ("TriviaQA / Natural Questions RAG baselines", 1, ["hydrate_retrieve"]),
    ("FEVER fact verification vs SUPERSEDES", 4, ["conflict_compose"]),
    ("VitaminC fact revision corpus", 4, ["conflict_compose"]),
    ("ConflictQA / conflicting knowledge eval", 1, ["conflict_compose"]),
    ("FreshQA temporal freshness eval", 1, ["hydrate_retrieve"]),
    ("RealtimeQA temporal memory", 1, ["hydrate_retrieve"]),
    ("SituatedQA / context-dependent answers", 1, ["hydrate_retrieve"]),
    ("DialDoc / document-grounded dialogue memory", 3, ["episode_cognify"]),
    ("MultiWOZ belief-state memory", 3, ["episode_cognify"]),
    ("SGD Schema-Guided Dialogue memory", 3, ["episode_cognify"]),
    ("Taskmaster dialogue memory", 3, ["episode_cognify"]),
    ("PersonaChat / personalization memory", 3, ["episode_cognify"]),
    ("MSC — Multi-Session Chat", 3, ["episode_cognify"]),
    ("Conversation Chronicles long dialogue", 3, ["episode_cognify"]),
    ("PerLTQA personal long-term QA", 1, ["hydrate_retrieve"]),
    ("Long-context Needle-in-Haystack protocols", 1, ["hydrate_retrieve"]),
    ("RULER long-context eval suite", 1, ["hydrate_retrieve"]),
    ("∞Bench long-context", 1, ["hydrate_retrieve"]),
    ("LongBench / LongBench-v2", 1, ["hydrate_retrieve"]),
    ("L-Eval long-context eval", 1, ["hydrate_retrieve"]),
    ("ZeroSCROLLS long-context", 1, ["hydrate_retrieve"]),
    ("QuALITY long-doc reading", 1, ["hydrate_retrieve"]),
    ("BookSum / chapter summarization memory", 3, ["episode_cognify"]),
    ("SummScreen dialogue summarization", 3, ["episode_cognify"]),
    ("MediaSum interview summarization", 3, ["episode_cognify"]),
    ("QMSum query-based meeting memory", 3, ["episode_cognify"]),
    ("MeetingBank meeting memory", 3, ["episode_cognify"]),
    ("AMI / ICSI meeting corpora (memory baselines)", 3, ["episode_cognify"]),
    ("TopicSeg classical text segmentation (Choi, etc.)", 3, ["episode_cognify"]),
    ("TextTiling classical boundary detection", 3, ["episode_cognify"]),
    ("C99 / TopicTiling segmentation", 3, ["episode_cognify"]),
    ("BERT-based dialogue discourse segmentation papers", 3, ["episode_cognify"]),
    ("SuperDialseg dialogue segmentation", 3, ["episode_cognify"]),
    ("DialSTART family follow-ons", 3, ["episode_cognify"]),
    ("GIMS / graph-informed memory systems (survey tails)", 4, ["anchors_graph"]),
    ("A-MEM follow-on notes / Zettelkasten agent memory", 4, ["anchors_graph"]),
    ("MemTree hierarchical memory tree", 3, ["episode_cognify"]),
    ("TiM follow-on think-in-memory variants", 3, ["episode_cognify"]),
    ("SCM controller variants beyond 2304.13343", 2, ["capture_working"]),
    ("Ebbinghaus forgetting implementations beyond MemoryBank", 2, ["capture_working"]),
    ("Human episodic memory models → agent mapping papers", 6, ["episode_cognify"]),
    ("Complementary learning systems (CLS) → L2/L3 mapping", 6, ["episode_cognify"]),
    ("Hopfield / modern Hopfield retrieval memory", 6, ["hydrate_retrieve"]),
    ("KAN / kernel memory analogies (supporting)", 6, ["hydrate_retrieve"]),
    ("Vector DB product memory patterns (Chroma/Weaviate/Qdrant)", 6, ["hydrate_retrieve"]),
    ("pgvector / sqlite-vss engineering memory notes", 6, ["hydrate_retrieve"]),
    ("CRDT primers for parallel compose (automerge/yjs)", 4, ["conflict_compose"]),
    ("Event sourcing primers for audit losers", 4, ["conflict_compose"]),
    ("CQRS read-model projections vs compose", 4, ["conflict_compose"]),
    ("Operational transform vs CRDT conflict notes", 4, ["conflict_compose"]),
    ("Anomaly detection for stale belief edges", 4, ["conflict_compose"]),
    ("Knowledge graph embedding entity resolve (TransE/RotatE)", 4, ["anchors_graph"]),
    ("Entity linking surveys (EL) for Anchor resolve", 4, ["anchors_graph"]),
    ("Coreference resolution for agent entity merge", 4, ["anchors_graph"]),
    ("OpenIE6 / IMoJIE extraction pipelines", 4, ["anchors_graph"]),
    ("SpaCy / GLINER IE engineering notes", 4, ["anchors_graph"]),
    ("LLM-as-extractor reliability studies", 1, ["anchors_graph"]),
    ("Hallucination audits for memory write paths", 1, ["conflict_compose"]),
    ("Self-RAG / CRAG corrective retrieval", 1, ["hydrate_retrieve"]),
    ("Corrective RAG (Yan et al.) full mechanisms", 1, ["hydrate_retrieve"]),
    ("Adaptive retrieval controllers beyond Adaptive-RAG", 6, ["hydrate_retrieve"]),
    ("FLARE active retrieval", 6, ["hydrate_retrieve"]),
    ("IRCoT interleaving retrieval", 6, ["hydrate_retrieve"]),
    ("DSP / Demonstrate-Search-Predict", 6, ["hydrate_retrieve"]),
    ("REPLUG retrieval-enhanced LMs", 6, ["hydrate_retrieve"]),
    ("Atlas few-shot retrieval memory", 6, ["hydrate_retrieve"]),
    ("REALM pretraining retrieval memory", 6, ["hydrate_retrieve"]),
    ("kNN-LM datastore memory", 6, ["hydrate_retrieve"]),
    ("SPALM / sparse memory LMs", 6, ["capture_working"]),
    ("Product Quantization memory indexes", 6, ["hydrate_retrieve"]),
    ("HNSW engineering notes for hydrate latency", 6, ["hydrate_retrieve"]),
    ("BM25 + dense hybrid retrieval recipes", 6, ["hydrate_retrieve"]),
    ("ColBERT late interaction retrieval", 6, ["hydrate_retrieve"]),
    ("BGE / E5 embedding model cards for memory", 6, ["hydrate_retrieve"]),
    ("Instruction-aware embeddings for agent memory", 6, ["hydrate_retrieve"]),
    ("Matryoshka embeddings for budgeted hydrate", 2, ["hydrate_retrieve"]),
    ("Prompt compression (LLMLingua / LongLLMLingua)", 2, ["capture_working"]),
    ("Selective Context / semantic compression", 2, ["capture_working"]),
    ("RECOMP retrieve-compress", 2, ["capture_working"]),
    ("xRAG / representation compression", 2, ["capture_working"]),
    ("Gisting / gist tokens memory", 2, ["capture_working"]),
    ("Activation Beacon / compressed KV", 2, ["capture_working"]),
    ("PyramidKV / multilevel KV eviction", 2, ["capture_working"]),
    ("Quest / KV retrieval for long context", 2, ["capture_working"]),
    ("LOOK-M multimodal KV memory", 2, ["capture_working"]),
    ("Heavy-Hitter variants beyond H₂O", 2, ["capture_working"]),
    ("Attention sink analyses beyond StreamingLLM", 2, ["capture_working"]),
    ("Scissorhands KV eviction", 2, ["capture_working"]),
    ("LESS / adaptive KV", 2, ["capture_working"]),
    ("Gear / quantized KV cache", 2, ["capture_working"]),
    ("KIVI KV cache quantization", 2, ["capture_working"]),
    ("SmoothQuant / KV quant engineering", 2, ["capture_working"]),
    ("vLLM paged attention engineering notes", 2, ["capture_working"]),
    ("SGLang radix attention prefix memory", 2, ["capture_working"]),
    ("Anthropic context editing API notes (beyond inventory)", 2, ["capture_working"]),
    ("OpenAI Responses / compaction API notes", 2, ["capture_working"]),
    ("Gemini context caching docs", 2, ["capture_working"]),
    ("AWS Bedrock session memory docs", 2, ["capture_working"]),
    ("Azure AI Agent Service memory docs", 2, ["capture_working"]),
    ("Google ADK session/memory docs", 2, ["capture_working"]),
    ("OpenAI Swarm / Agents SDK memory patterns", 6, ["capture_working"]),
    ("Semantic Kernel memory store", 6, ["hydrate_retrieve"]),
    ("Haystack Agent memory components", 6, ["hydrate_retrieve"]),
    ("DSPy memory / state modules", 6, ["hydrate_retrieve"]),
    ("Guidance / Outlines constrained decode + memory", 6, ["capture_working"]),
    ("PydanticAI deps/memory patterns", 6, ["capture_working"]),
    ("Temporal.io durable execution vs episode boundaries", 3, ["episode_cognify"]),
    ("Cadence/workflow engines as episode stores", 3, ["episode_cognify"]),
    ("OpenTelemetry span→episode mapping", 3, ["episode_cognify"]),
    ("OTel GenAI semantic conventions for L0 capture", 2, ["capture_working"]),
    ("LLM tracing (Langfuse/Phoenix) → Evidence mapping", 2, ["capture_working"]),
    ("Prompt logging redaction standards", 5, ["privacy_seal"]),
    ("PII detection libraries for capture redaction", 5, ["privacy_seal"]),
    ("Presidio / common redaction engines", 5, ["privacy_seal"]),
    ("DLP patterns for agent transcripts", 5, ["privacy_seal"]),
    ("Secret scanning (trufflehog/gitleaks) at capture", 5, ["privacy_seal"]),
    ("OWASP LLM Top 10 — sensitive info disclosure", 5, ["privacy_seal"]),
    ("OWASP Agentic AI security draft", 5, ["privacy_seal"]),
    ("NIST AI RMF memory/governance mapping", 5, ["privacy_seal"]),
    ("Contextual integrity (Nissenbaum) primers", 5, ["privacy_seal"]),
    ("GDPR right-to-erasure vs invalidate+audit", 5, ["privacy_seal"]),
    ("CCPA deletion vs belief history retention", 5, ["privacy_seal"]),
    ("Differential privacy for shared memory aggregates", 5, ["privacy_seal"]),
    ("Secure enclaves for sealed packs (SGX/SEV notes)", 5, ["privacy_seal"]),
    ("TPM / hardware key custody for .kpack", 5, ["privacy_seal"]),
    ("age / ssh-age recipient patterns beyond C2SP", 5, ["privacy_seal"]),
    ("TUF / update frameworks for pack distribution", 5, ["privacy_seal"]),
    ("Sigstore / keyless signing for shareable anchors", 5, ["privacy_seal"]),
    ("Paseto / Branca token capability notes", 5, ["privacy_seal"]),
    ("Biscuit vs Macaroon attenuation cookbook", 5, ["privacy_seal"]),
    ("UCANs — user-controlled authorization networks", 5, ["privacy_seal"]),
    ("Object capabilities (Miller) deep primer", 5, ["privacy_seal"]),
    ("Spritely Goblins / OcapPub deeper docs", 5, ["privacy_seal"]),
    ("Cap'n Proto RPC capability patterns", 5, ["privacy_seal"]),
    ("E language capability lessons for agents", 5, ["privacy_seal"]),
    ("Macaroons caveats engineering cookbook", 5, ["privacy_seal"]),
    ("Google Zanzibar authorization for shared graphs", 5, ["privacy_seal"]),
    ("OPA / Cedar policy engines for compose gates", 5, ["privacy_seal"]),
    ("SpiceDB relationship tuples vs Anchor ACL", 5, ["privacy_seal"]),
    ("ReBAC surveys for shareable anchors", 5, ["privacy_seal"]),
    ("ABAC vs capability trade studies", 5, ["privacy_seal"]),
    ("Confused deputy problem classics", 5, ["privacy_seal"]),
    ("Ambient authority anti-patterns in agent tools", 5, ["privacy_seal"]),
    ("Prompt injection → memory poisoning papers", 5, ["privacy_seal"]),
    ("Indirect prompt injection memory persistence", 5, ["privacy_seal"]),
    ("RAG poisoning / corpus poisoning papers", 5, ["privacy_seal"]),
    ("Agent malware / tool exfil case studies", 5, ["privacy_seal"]),
    ("MemGuard / memory firewall product notes", 5, ["privacy_seal"]),
    ("Air-gapped memory partitions engineering", 5, ["privacy_seal"]),
    ("Cross-tenant vector index isolation failures", 5, ["privacy_seal"]),
    ("Embedding inversion / recovery attacks", 5, ["privacy_seal"]),
    ("Membership inference on memory stores", 5, ["privacy_seal"]),
    ("Model stealing via memory APIs", 5, ["privacy_seal"]),
    ("Canary / watermark insertion for memory provenance", 5, ["privacy_seal"]),
    ("Provenance graphs for LLM outputs (survey)", 4, ["conflict_compose"]),
    ("W3C PROV mapping to Evidence rows", 4, ["conflict_compose"]),
    ("Datasheets for memory datasets", 1, ["hydrate_retrieve"]),
    ("Model cards for memory controllers", 6, ["hydrate_retrieve"]),
    ("HELM / decoding trust eval suites", 1, ["hydrate_retrieve"]),
    ("BIG-bench agent-adjacent tasks", 1, ["hydrate_retrieve"]),
    ("MMLU as non-memory control baseline", 1, ["hydrate_retrieve"]),
    ("AgentBoard evaluation framework", 1, ["hydrate_retrieve"]),
    ("AgentEval / LLM-as-judge for agents", 1, ["hydrate_retrieve"]),
    ("LLM-as-judge bias studies (memory claims)", 1, ["hydrate_retrieve"]),
    ("Inter-annotator agreement for eng-judgment gold", 6, ["hydrate_retrieve"]),
    ("Pairwise preference protocols for compose quality", 6, ["conflict_compose"]),
    ("Bradley-Terry ranking for memory ablations", 6, ["hydrate_retrieve"]),
    ("Cost/latency accounting for memory maintenance", 6, ["capture_working"]),
    ("Token economics of reflection loops", 6, ["episode_cognify"]),
    ("Sleep-time compute papers (beyond Sleep-SCM)", 3, ["episode_cognify"]),
    ("DreamBooth-style consolidation analogies (supporting)", 6, ["episode_cognify"]),
    ("Continual learning surveys → agent memory", 6, ["episode_cognify"]),
    ("Catastrophic forgetting in parametric memory", 6, ["capture_working"]),
    ("Elastic Weight Consolidation analogies", 6, ["capture_working"]),
    ("Progress & compress continual learning", 6, ["capture_working"]),
    ("PackNet / progressive nets analogies", 6, ["capture_working"]),
    ("Experience replay buffers (RL) → L2 mapping", 3, ["episode_cognify"]),
    ("Prioritized experience replay", 3, ["episode_cognify"]),
    ("Episodic control (Neural Episodic Control)", 3, ["episode_cognify"]),
    ("Model-based RL world models as memory", 6, ["episode_cognify"]),
    ("Dreamer / RSSM latent memory", 6, ["episode_cognify"]),
    ("Decision Transformer trajectory memory", 6, ["episode_cognify"]),
    ("Trajectory transformer memory", 6, ["episode_cognify"]),
    ("Offline RL datasets as episodic corpora", 3, ["episode_cognify"]),
    ("Case-based reasoning classics → Memento mapping", 3, ["episode_cognify"]),
    ("Rete / production systems as procedural memory", 6, ["episode_cognify"]),
    ("SOAR / ACT-R cognitive architectures mapping", 6, ["episode_cognify"]),
    ("Global Workspace Theory → hydrate broadcast", 6, ["hydrate_retrieve"]),
    ("Predictive processing / surprise → EST", 3, ["episode_cognify"]),
    ("Free energy principle primers (supporting only)", 6, ["episode_cognify"]),
    ("Event Segmentation Theory psychology sources", 3, ["episode_cognify"]),
    ("Zettelkasten method primers for A-MEM mapping", 4, ["anchors_graph"]),
    ("Personal knowledge management (PKM) systems", 6, ["anchors_graph"]),
    ("Roam/Logseq/Obsidian graph UX lessons", 4, ["anchors_graph"]),
    ("Org-roam / emacs memory workflows", 6, ["anchors_graph"]),
    ("Dendron hierarchical notes", 6, ["anchors_graph"]),
    ("Tana / supertags as schema memory", 6, ["anchors_graph"]),
    ("ADR / Architecture Decision Records practice", 6, ["conflict_compose"]),
    ("QOC — Questions Options Criteria rationale", 6, ["conflict_compose"]),
    ("IBIS issue-based information systems", 6, ["conflict_compose"]),
    ("Design rationale capture systems", 6, ["conflict_compose"]),
    ("Software provenance / SBOM analogies", 5, ["privacy_seal"]),
    ("SLSA build provenance for pack integrity", 5, ["privacy_seal"]),
    ("in-toto supply chain attestation", 5, ["privacy_seal"]),
    ("Reproducible builds for memory fixtures", 6, ["hydrate_retrieve"]),
    ("Property-based testing for SUPERSEDES", 4, ["conflict_compose"]),
    ("Jepsen-style linearizability lessons for compose", 4, ["conflict_compose"]),
    ("CALM theorem / coordination-free compose", 4, ["conflict_compose"]),
    ("BAC / BASE consistency for agent memory", 4, ["conflict_compose"]),
    ("Causal consistency primers for multi-writer Anchors", 4, ["conflict_compose"]),
    ("Vector clocks / version vectors", 4, ["conflict_compose"]),
    ("Merkle clocks / hash chains for audit", 4, ["conflict_compose"]),
    ("Tamper-evident logs (Trillian) analogies", 5, ["privacy_seal"]),
    ("Certificate Transparency lessons for Anchor audit", 5, ["privacy_seal"]),
    ("Append-only Evidence store designs", 4, ["conflict_compose"]),
    ("Soft deletion vs hard deletion studies", 4, ["conflict_compose"]),
    ("GDPR Article 17 technical implementations", 5, ["privacy_seal"]),
    ("Right to be forgotten in ML surveys", 5, ["privacy_seal"]),
    ("Machine unlearning surveys → Anchor invalidate", 5, ["privacy_seal"]),
    ("SISA unlearning → partition memory stores", 5, ["privacy_seal"]),
    ("Exact unlearning vs approximate for graphs", 5, ["privacy_seal"]),
    ("Graph unlearning papers", 5, ["privacy_seal"]),
    ("Federated learning memory silos", 5, ["privacy_seal"]),
    ("Split learning / vertical privacy", 5, ["privacy_seal"]),
    ("Secure multi-party compute for shared stats", 5, ["privacy_seal"]),
    ("Homomorphic encryption feasibility for packs", 5, ["privacy_seal"]),
    ("Searchable encryption for private hydrate", 5, ["privacy_seal"]),
    ("PIR private information retrieval for memory", 5, ["privacy_seal"]),
    ("ORAM for access-pattern hiding (supporting)", 5, ["privacy_seal"]),
    ("TEE-based RAG papers", 5, ["privacy_seal"]),
    ("Confidential computing for LLM inference", 5, ["privacy_seal"]),
    ("Private retrieval / anonymized shared memory", 5, ["privacy_seal"]),
    ("k-anonymity / l-diversity for shared digests", 5, ["privacy_seal"]),
    ("Synthetic data for shareable episode digests", 5, ["privacy_seal"]),
    ("Differential privacy for community summaries", 5, ["privacy_seal"]),
    ("Watermarking shared Anchor statements", 5, ["privacy_seal"]),
    ("Canary tokens in Evidence for exfil detect", 5, ["privacy_seal"]),
    ("Honeytokens in agent memory", 5, ["privacy_seal"]),
    ("Audit logging best practices (NIST 800-92)", 5, ["privacy_seal"]),
    ("SOC2 evidence mapping for memory products", 6, ["privacy_seal"]),
    ("ISO 27001 controls for agent memory stores", 6, ["privacy_seal"]),
    ("Threat modeling (STRIDE) for Kedger surfaces", 5, ["privacy_seal"]),
    ("Abuse cases for share/unshare cascades", 5, ["privacy_seal"]),
    ("Red-team playbooks for memory exfiltration", 5, ["privacy_seal"]),
    ("Purple-team eval loops for Inv-Scope", 1, ["privacy_seal"]),
    ("Chaos engineering for compose projections", 4, ["conflict_compose"]),
    ("Fault injection in boundary detectors", 3, ["episode_cognify"]),
    ("Clock skew / bi-temporal correctness tests", 4, ["anchors_graph"]),
    ("Time-zone / session idle boundary edge cases", 3, ["episode_cognify"]),
    ("Multi-device session continuity memory", 3, ["episode_cognify"]),
    ("Mobile/offline agent memory sync", 4, ["conflict_compose"]),
    ("CRDT-backed notes apps (case studies)", 4, ["conflict_compose"]),
    ("Local-first software (Kleppmann) primers", 4, ["conflict_compose"]),
    ("Automerge paper + docs", 4, ["conflict_compose"]),
    ("Yjs CRDT docs", 4, ["conflict_compose"]),
    ("Diamond Types / Loro CRDT notes", 4, ["conflict_compose"]),
    ("MQTT / sync protocols for edge agents", 6, ["capture_working"]),
    ("Edge LLM memory constraints papers", 2, ["capture_working"]),
    ("On-device KV cache budgets", 2, ["capture_working"]),
    ("Speculative decoding + memory interaction", 2, ["capture_working"]),
    ("Prefill/decode disaggregation ops notes", 2, ["capture_working"]),
    ("Prefix caching hit-rate studies", 2, ["capture_working"]),
    ("Prompt cache economics", 2, ["capture_working"]),
    ("Session affinity for sticky working state", 2, ["capture_working"]),
    ("Sticky vs stateless hydrate service design", 6, ["hydrate_retrieve"]),
    ("Sidecar memory daemon architectures", 6, ["capture_working"]),
    ("eBPF capture of tool I/O (experimental)", 2, ["capture_working"]),
    ("FSEvents / inotify for repo memory capture", 2, ["capture_working"]),
    ("LSP / IDE hook capture surfaces", 2, ["capture_working"]),
    ("MCP tool-call logging schemas", 2, ["capture_working"]),
    ("OpenAI tool/function call transcript schemas", 2, ["capture_working"]),
    ("Anthropic tool_use block schemas", 2, ["capture_working"]),
    ("Gemini function calling schemas", 2, ["capture_working"]),
    ("Unified tool-call normalized L0 schema proposals", 2, ["capture_working"]),
    ("JSONL episode interchange formats", 3, ["episode_cognify"]),
    ("OpenTelemetry GenAI events → L0 mapping cookbook", 2, ["capture_working"]),
    ("Parquet columnar Evidence lakes", 6, ["hydrate_retrieve"]),
    ("DuckDB analytical queries over L0", 6, ["hydrate_retrieve"]),
    ("SQLite FTS5 for Anchor search", 6, ["hydrate_retrieve"]),
    ("sqlite-graph / recursive CTE graph walks", 4, ["anchors_graph"]),
    ("Recursive SQL PPR approximations", 4, ["anchors_graph"]),
    ("Graph databases (Neo4j/Memgraph) for Anchors", 4, ["anchors_graph"]),
    ("Apache AGE / PG graph extensions", 4, ["anchors_graph"]),
    ("RDF / property graph impedance notes", 4, ["anchors_graph"]),
    ("SHACL shapes for Anchor validation", 4, ["anchors_graph"]),
    ("JSON Schema for sealed pack manifests", 5, ["privacy_seal"]),
    ("CBOR / deterministic encoding for packs", 5, ["privacy_seal"]),
    ("Canonical JSON (RFC 8785) for signatures", 5, ["privacy_seal"]),
    ("JWS / JWE for capability tokens", 5, ["privacy_seal"]),
    ("DPoP / sender-constrained tokens", 5, ["privacy_seal"]),
    ("OAuth RAR rich authorization for tools", 5, ["privacy_seal"]),
    ("GNAP authorization for agents", 5, ["privacy_seal"]),
    ("WIP agent identity standards (IETF/W3C)", 5, ["privacy_seal"]),
    ("DID / VC for agent identity (supporting)", 5, ["privacy_seal"]),
    ("Key Transparency for recipient directories", 5, ["privacy_seal"]),
    ("MLS architecture deeper than RFC skim", 5, ["privacy_seal"]),
    ("S/MIME vs age for pack encryption tradeoffs", 5, ["privacy_seal"]),
    ("PGP UX failure studies → key UX lessons", 5, ["privacy_seal"]),
    ("Magic Wormhole UX studies", 5, ["privacy_seal"]),
    ("QR / short-code pairing for sealed handoff", 5, ["privacy_seal"]),
    ("Airgap transfer patterns for .kpack", 5, ["privacy_seal"]),
    ("USB/sneakernet threat model for packs", 5, ["privacy_seal"]),
    ("Secure deletion / crypto shredding", 5, ["privacy_seal"]),
    ("Forward secrecy for reseal chains", 5, ["privacy_seal"]),
    ("Post-compromise security for shared graphs", 5, ["privacy_seal"]),
    ("Key rotation playbooks for sealed packs", 5, ["privacy_seal"]),
    ("Backup / recovery of memory roots", 5, ["privacy_seal"]),
    ("Shamir secret sharing for recovery", 5, ["privacy_seal"]),
    ("Social recovery for capability roots", 5, ["privacy_seal"]),
    ("Hardware security keys (FIDO) for unseal", 5, ["privacy_seal"]),
    ("Passkeys for developer unseal UX", 5, ["privacy_seal"]),
    ("Enterprise SSO gating for hydrate", 5, ["privacy_seal"]),
    ("SCIM provisioning for agent memory tenants", 5, ["privacy_seal"]),
    ("Multi-tenant row-level security patterns", 5, ["privacy_seal"]),
    ("Postgres RLS recipes for Anchor visibility", 5, ["privacy_seal"]),
    ("Attribute-based row filters vs capability checks", 5, ["privacy_seal"]),
    ("Policy-as-code tests for Inv-Scope", 5, ["privacy_seal"]),
    ("Formal verification lite for SUPERSEDES", 4, ["conflict_compose"]),
    ("TLA+ specs for bi-temporal invalidation", 4, ["conflict_compose"]),
    ("Alloy models for conflict sets", 4, ["conflict_compose"]),
    ("Property tests for promotion gates", 4, ["anchors_graph"]),
    ("Mutation testing for boundary detector", 3, ["episode_cognify"]),
    ("Golden transcript fixtures methodology", 1, ["hydrate_retrieve"]),
    ("Synthetic eng dialogue generators for eval", 1, ["hydrate_retrieve"]),
    ("Bug-injection into memory graphs for eval", 1, ["conflict_compose"]),
    ("Counterfactual episode edits for causal eval", 1, ["episode_cognify"]),
    ("Ablation protocols for Heat/recurrence thresholds", 1, ["episode_cognify"]),
    ("Sensitivity analysis for PPR damping 0.5", 1, ["anchors_graph"]),
    ("Threshold search methods for synonym τ=0.8", 1, ["anchors_graph"]),
    ("Human preference collection for eng-judgment", 6, ["hydrate_retrieve"]),
    ("Interleaved A/B for compose projections", 6, ["conflict_compose"]),
    ("Latency SLOs for cognify cron", 6, ["episode_cognify"]),
    ("Cost SLOs for LLM extraction calls", 6, ["capture_working"]),
    ("Cache hit metrics for hydrate", 6, ["hydrate_retrieve"]),
    ("Drift detectors for embedding upgrades", 6, ["hydrate_retrieve"]),
    ("Re-embedding migration playbooks", 6, ["hydrate_retrieve"]),
    ("Schema migration for memory SQLite", 6, ["anchors_graph"]),
    ("Backward-compatible Anchor kind evolution", 6, ["anchors_graph"]),
    ("Deprecation of Evidence fields", 6, ["conflict_compose"]),
    ("Versioned sealed pack manifests", 5, ["privacy_seal"]),
    ("Compatibility matrix across Kedger CLI versions", 6, ["privacy_seal"]),
    ("Migration from MoDeX historical labels → Kedger", 6, ["capture_working"]),
    ("Survey seed: Agent Memory Paper List (Shichun-Liu) index crawl", 6, ["hydrate_retrieve"]),
    ("Survey seed: papers citing 2512.13564 (long tail)", 6, ["hydrate_retrieve"]),
    ("Survey seed: papers citing 2603.07670 (long tail)", 6, ["hydrate_retrieve"]),
    ("Survey seed: papers citing 2602.05665 (graph memory)", 4, ["anchors_graph"]),
    ("Survey seed: papers citing 2309.07864 (§memory)", 6, ["episode_cognify"]),
    ("Survey seed: papers citing 2602.19320 (anatomy/eval)", 1, ["hydrate_retrieve"]),
    ("Survey seed: papers citing 2605.06716 (experience stage)", 3, ["episode_cognify"]),
    ("Survey seed: papers citing MemClaw / governed shared memory", 5, ["privacy_seal"]),
    ("Survey seed: papers citing AgentLeak", 5, ["privacy_seal"]),
    ("Survey seed: papers citing Collaborative Memory 2505.18279", 5, ["privacy_seal"]),
    ("Survey seed: Graphiti citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: HippoRAG citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: MemGPT citation neighborhood", 2, ["capture_working"]),
    ("Survey seed: Generative Agents citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: LoCoMo citation neighborhood", 1, ["hydrate_retrieve"]),
    ("Survey seed: LongMemEval citation neighborhood", 1, ["hydrate_retrieve"]),
    ("Survey seed: MemoryAgentBench citation neighborhood", 1, ["hydrate_retrieve"]),
    ("Survey seed: StreamingLLM citation neighborhood", 2, ["capture_working"]),
    ("Survey seed: GraphRAG citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: RAG (Lewis 2005.11401) citation neighborhood", 6, ["hydrate_retrieve"]),
    ("Survey seed: ReAct citation neighborhood", 2, ["capture_working"]),
    ("Survey seed: Reflexion citation neighborhood", 2, ["capture_working"]),
    ("Survey seed: Voyager skill-library neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: ConfAIde citation neighborhood", 5, ["privacy_seal"]),
    ("Survey seed: Fides IFC citation neighborhood", 5, ["privacy_seal"]),
    ("Survey seed: StateFuse citation neighborhood", 4, ["conflict_compose"]),
    ("Survey seed: TOKI citation neighborhood", 4, ["conflict_compose"]),
    ("Survey seed: Nemori / EST citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: RecMem citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: ES-Mem citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: MemoryOS citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: A-MEM citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: Mem0 citation neighborhood", 4, ["conflict_compose"]),
    ("Survey seed: LightMem citation neighborhood", 2, ["capture_working"]),
    ("Survey seed: MAGMA citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: Memory-R1 citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: ReasoningBank citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: MEM1 citation neighborhood", 2, ["capture_working"]),
    ("Survey seed: LEGOMem citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: MemAct citation neighborhood", 2, ["capture_working"]),
    ("Survey seed: O-Mem citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: Agent KB citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: H-Mem citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: DialSim citation neighborhood", 1, ["hydrate_retrieve"]),
    ("Survey seed: MemoryBench citation neighborhood", 1, ["hydrate_retrieve"]),
    ("Survey seed: RAPTOR citation neighborhood", 6, ["hydrate_retrieve"]),
    ("Survey seed: PropRAG citation neighborhood", 6, ["hydrate_retrieve"]),
    ("Survey seed: Adaptive-RAG citation neighborhood", 6, ["hydrate_retrieve"]),
    ("Survey seed: Selective Memory / supersession neighborhood", 4, ["conflict_compose"]),
    ("Survey seed: AssoMem citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: Mem-α citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: MemGAS citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: HyperGraphRAG citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: SSGM citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: G-Memory citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: AriGraph citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: EM-LLM citation neighborhood", 3, ["episode_cognify"]),
    ("Survey seed: LightRAG citation neighborhood", 4, ["anchors_graph"]),
    ("Survey seed: PRISM citation neighborhood", 5, ["privacy_seal"]),
    ("Survey seed: MemLeak citation neighborhood", 5, ["privacy_seal"]),
    ("Survey seed: MetaGPT memory implications", 4, ["conflict_compose"]),
    ("Survey seed: ChatDev memory implications", 4, ["conflict_compose"]),
    ("Survey seed: CAMEL memory implications", 4, ["conflict_compose"]),
    ("Survey seed: AutoGen memory implications", 4, ["conflict_compose"]),
    ("Survey seed: multi-agent collaboration survey 2501.06322 tails", 4, ["conflict_compose"]),
    ("Survey seed: AI long-term memory survey 2411.00489 tails", 6, ["anchors_graph"]),
    ("Survey seed: From Human Memory to AI Memory 2504.15965 tails", 6, ["episode_cognify"]),
    ("Survey seed: Agent Memory Second Half 2602.06052 tails", 6, ["hydrate_retrieve"]),
    ("Survey seed: Zhang 2404.13501 bibliography long tail", 2, ["capture_working"]),
    ("Survey seed: Memory in Age of AI Agents bibliography long tail A", 6, ["hydrate_retrieve"]),
    ("Survey seed: Memory in Age of AI Agents bibliography long tail B", 6, ["hydrate_retrieve"]),
    ("Survey seed: Memory in Age of AI Agents bibliography long tail C", 6, ["hydrate_retrieve"]),
    ("Survey seed: Memory for Autonomous LLM Agents bibliography A", 6, ["anchors_graph"]),
    ("Survey seed: Memory for Autonomous LLM Agents bibliography B", 6, ["anchors_graph"]),
    ("Survey seed: Graph-based Agent Memory bibliography A", 4, ["anchors_graph"]),
    ("Survey seed: Graph-based Agent Memory bibliography B", 4, ["anchors_graph"]),
    ("Survey seed: Anatomy of Agentic Memory bibliography A", 1, ["hydrate_retrieve"]),
    ("Survey seed: Anatomy of Agentic Memory bibliography B", 1, ["hydrate_retrieve"]),
    ("Survey seed: From Storage to Experience bibliography A", 3, ["episode_cognify"]),
    ("Survey seed: From Storage to Experience bibliography B", 3, ["episode_cognify"]),
    ("Survey seed: Rise of LLM Agents bibliography memory slice A", 6, ["episode_cognify"]),
    ("Survey seed: Rise of LLM Agents bibliography memory slice B", 6, ["episode_cognify"]),
    ("Placeholder: unnamed toolkit README batch (OpenMemory cluster)", 4, ["anchors_graph"]),
    ("Placeholder: unnamed leakage paper cited by MemClaw #1", 5, ["privacy_seal"]),
    ("Placeholder: unnamed leakage paper cited by MemClaw #2", 5, ["privacy_seal"]),
    ("Placeholder: unnamed leakage paper cited by MemClaw #3", 5, ["privacy_seal"]),
    ("Placeholder: unnamed leakage paper cited by AgentLeak #1", 5, ["privacy_seal"]),
    ("Placeholder: unnamed leakage paper cited by AgentLeak #2", 5, ["privacy_seal"]),
    ("Placeholder: remaining MemClaw-cited governance paper", 5, ["privacy_seal"]),
    ("Placeholder: remaining PRISM-cited disclosure paper", 5, ["privacy_seal"]),
    ("Placeholder: VAULT follow-on / related KG disclosure", 5, ["privacy_seal"]),
    ("Placeholder: MAMA ACL'26 related topology papers", 5, ["privacy_seal"]),
    ("Placeholder: Clean REBEL PDF (non-arXiv canonical)", 4, ["anchors_graph"]),
    ("Placeholder: Stanford OpenIE canonical non-arXiv PDF", 4, ["anchors_graph"]),
    ("Placeholder: eng-judgment rubric sources (internal)", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger eval fixture design notes", 1, ["hydrate_retrieve"]),
    ("Placeholder: Kedger failure taxonomy worksheet", 1, ["hydrate_retrieve"]),
    ("Placeholder: capture redaction golden tests corpus", 2, ["capture_working"]),
    ("Placeholder: compaction budget ablation suite", 2, ["capture_working"]),
    ("Placeholder: episode boundary disagreement corpus", 3, ["episode_cognify"]),
    ("Placeholder: graph conflict tournament fixtures", 4, ["conflict_compose"]),
    ("Placeholder: privacy probe pack (Inv-Scope)", 5, ["privacy_seal"]),
    ("Placeholder: capability attenuation cookbook cases", 5, ["privacy_seal"]),
    ("Placeholder: eng-judgment pairwise label guide", 6, ["hydrate_retrieve"]),
    ("Placeholder: metric card — recall@k hydrate", 1, ["hydrate_retrieve"]),
    ("Placeholder: metric card — conflict loser audit rate", 1, ["conflict_compose"]),
    ("Placeholder: metric card — boundary F1", 1, ["episode_cognify"]),
    ("Placeholder: metric card — compaction token save vs utility", 1, ["capture_working"]),
    ("Placeholder: metric card — Inv-Scope violation rate", 1, ["privacy_seal"]),
    ("Placeholder: metric card — eng-judgment win rate", 6, ["hydrate_retrieve"]),
    ("Placeholder: refine loop — threshold retune protocol", 6, ["episode_cognify"]),
    ("Placeholder: refine loop — PPR damping sweep", 4, ["anchors_graph"]),
    ("Placeholder: refine loop — Heat τ sensitivity", 3, ["episode_cognify"]),
    ("Placeholder: refine loop — synonym τ sensitivity", 4, ["anchors_graph"]),
    ("Placeholder: refine loop — idle boundary minutes", 3, ["episode_cognify"]),
    ("Placeholder: refine loop — pressure warn/flush", 2, ["capture_working"]),
    ("Placeholder: bibliography harvest pass — survey HTML citations", 6, ["hydrate_retrieve"]),
    ("Placeholder: bibliography harvest pass — Batch2 refs", 6, ["hydrate_retrieve"]),
    ("Placeholder: bibliography harvest pass — Batch3 refs", 6, ["hydrate_retrieve"]),
    ("Placeholder: bibliography harvest pass — P1 cards refs", 2, ["capture_working"]),
    ("Placeholder: bibliography harvest pass — P2 cards refs", 3, ["episode_cognify"]),
    ("Placeholder: bibliography harvest pass — P3 cards refs", 4, ["anchors_graph"]),
    ("Placeholder: bibliography harvest pass — P4 cards refs", 4, ["conflict_compose"]),
    ("Placeholder: bibliography harvest pass — P5 cards refs", 6, ["hydrate_retrieve"]),
    ("Placeholder: bibliography harvest pass — P6 cards refs", 5, ["privacy_seal"]),
    ("Placeholder: bibliography harvest pass — SHAREABLE memo refs", 5, ["privacy_seal"]),
    ("Placeholder: bibliography harvest pass — SEALED_PACK refs", 5, ["privacy_seal"]),
    ("Placeholder: bibliography harvest pass — PARALLEL compose refs", 4, ["conflict_compose"]),
    ("Placeholder: future arXiv alert — agent memory 2026 Q3", 6, ["hydrate_retrieve"]),
    ("Placeholder: future arXiv alert — privacy agents 2026 Q3", 5, ["privacy_seal"]),
    ("Placeholder: future arXiv alert — long-context KV 2026 Q3", 2, ["capture_working"]),
    ("Placeholder: future arXiv alert — multi-agent conflict 2026 Q3", 4, ["conflict_compose"]),
    ("Placeholder: future arXiv alert — episode segmentation 2026 Q3", 3, ["episode_cognify"]),
    ("Placeholder: future arXiv alert — eval suites 2026 Q3", 1, ["hydrate_retrieve"]),
    ("Placeholder: workshop papers — agent memory NeurIPS/ICML tails", 6, ["hydrate_retrieve"]),
    ("Placeholder: workshop papers — LLM privacy tails", 5, ["privacy_seal"]),
    ("Placeholder: blog/engineering — Letta memory deep dives", 2, ["capture_working"]),
    ("Placeholder: blog/engineering — Graphiti temporal edges", 4, ["anchors_graph"]),
    ("Placeholder: blog/engineering — Anthropic compaction", 2, ["capture_working"]),
    ("Placeholder: blog/engineering — Cursor hooks recipes", 2, ["capture_working"]),
    ("Placeholder: standards track — MCP memory resources", 2, ["capture_working"]),
    ("Placeholder: standards track — agent authz drafts", 5, ["privacy_seal"]),
    ("Placeholder: standards track — pack manifest interop", 5, ["privacy_seal"]),
    ("Placeholder: community list — awesome-agent-memory", 6, ["hydrate_retrieve"]),
    ("Placeholder: community list — awesome-llm-memory", 6, ["hydrate_retrieve"]),
    ("Placeholder: community list — awesome-rag", 6, ["hydrate_retrieve"]),
    ("Placeholder: community list — awesome-graph-rag", 4, ["anchors_graph"]),
    ("Placeholder: thesis/tech-report — agent memory long tails A", 6, ["hydrate_retrieve"]),
    ("Placeholder: thesis/tech-report — agent memory long tails B", 6, ["hydrate_retrieve"]),
    ("Placeholder: thesis/tech-report — agent memory long tails C", 6, ["hydrate_retrieve"]),
    ("Placeholder: industry whitepaper — enterprise agent memory", 6, ["privacy_seal"]),
    ("Placeholder: industry whitepaper — AI governance memory", 5, ["privacy_seal"]),
    ("Placeholder: patent landscape skim — agent memory (non-normative)", 6, ["hydrate_retrieve"]),
    ("Placeholder: related OSS — Mem0 server internals", 4, ["anchors_graph"]),
    ("Placeholder: related OSS — Zep server internals", 4, ["anchors_graph"]),
    ("Placeholder: related OSS — GraphRAG toolkit forks", 4, ["anchors_graph"]),
    ("Placeholder: related OSS — LightRAG forks", 4, ["anchors_graph"]),
    ("Placeholder: related OSS — HippoRAG reproduction", 4, ["anchors_graph"]),
    ("Placeholder: related OSS — A-MEM reproduction", 4, ["anchors_graph"]),
    ("Placeholder: related OSS — MemoryOS reproduction", 3, ["episode_cognify"]),
    ("Placeholder: related OSS — Nemori reproduction", 3, ["episode_cognify"]),
    ("Placeholder: related OSS — RecMem reproduction", 3, ["episode_cognify"]),
    ("Placeholder: related OSS — ES-Mem reproduction", 3, ["episode_cognify"]),
    ("Placeholder: related OSS — MemGPT/Letta reproduction notes", 2, ["capture_working"]),
    ("Placeholder: related OSS — StreamingLLM reference", 2, ["capture_working"]),
    ("Placeholder: related OSS — SnapKV reference", 2, ["capture_working"]),
    ("Placeholder: related OSS — H2O reference", 2, ["capture_working"]),
    ("Placeholder: related OSS — ConfAIde eval harness", 1, ["privacy_seal"]),
    ("Placeholder: related OSS — LoCoMo eval harness", 1, ["hydrate_retrieve"]),
    ("Placeholder: related OSS — LongMemEval harness", 1, ["hydrate_retrieve"]),
    ("Placeholder: related OSS — MemoryAgentBench harness", 1, ["hydrate_retrieve"]),
    ("Placeholder: related OSS — DialSim harness", 1, ["hydrate_retrieve"]),
    ("Placeholder: related OSS — MemoryBench harness", 1, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot A", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot B", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot C", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot D", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot E", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot F", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot G", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot H", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot I", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot J", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot K", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot L", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot M", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot N", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot O", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot P", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot Q", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot R", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot S", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot T", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot U", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot V", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot W", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot X", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot Y", 6, ["hydrate_retrieve"]),
    ("Placeholder: Kedger Track0 runway overflow slot Z", 6, ["hydrate_retrieve"]),
    ("Placeholder: bibliography harvest — SHAREABLE non-arXiv cluster", 5, ["privacy_seal"]),
    ("Placeholder: bibliography harvest — crypto capability cluster", 5, ["privacy_seal"]),
    ("Placeholder: bibliography harvest — eval failure cluster", 1, ["hydrate_retrieve"]),
    ("Placeholder: bibliography harvest — capture compaction cluster", 2, ["capture_working"]),
    ("Placeholder: bibliography harvest — episode boundary cluster", 3, ["episode_cognify"]),
    ("Placeholder: bibliography harvest — graph conflict cluster", 4, ["anchors_graph"]),
    ("Placeholder: bibliography harvest — eng-judgment cluster", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #1", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #2", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #3", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #4", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #5", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #6", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #7", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #8", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #9", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed system #10", 6, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed eval #1", 1, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed eval #2", 1, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed eval #3", 1, ["hydrate_retrieve"]),
    ("Placeholder: unnamed survey-indexed privacy #1", 5, ["privacy_seal"]),
    ("Placeholder: unnamed survey-indexed privacy #2", 5, ["privacy_seal"]),
    ("Placeholder: unnamed survey-indexed privacy #3", 5, ["privacy_seal"]),
    ("Placeholder: unnamed survey-indexed graph #1", 4, ["anchors_graph"]),
    ("Placeholder: unnamed survey-indexed graph #2", 4, ["anchors_graph"]),
    ("Placeholder: unnamed survey-indexed graph #3", 4, ["anchors_graph"]),
    ("Placeholder: unnamed survey-indexed episode #1", 3, ["episode_cognify"]),
    ("Placeholder: unnamed survey-indexed episode #2", 3, ["episode_cognify"]),
    ("Placeholder: unnamed survey-indexed episode #3", 3, ["episode_cognify"]),
    ("Placeholder: unnamed survey-indexed capture #1", 2, ["capture_working"]),
    ("Placeholder: unnamed survey-indexed capture #2", 2, ["capture_working"]),
    ("Placeholder: unnamed survey-indexed capture #3", 2, ["capture_working"]),
    ("Placeholder: runway pad — fetch-needed seed 001", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 002", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 003", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 004", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 005", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 006", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 007", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 008", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 009", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 010", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 011", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 012", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 013", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 014", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 015", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 016", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 017", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 018", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 019", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 020", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 021", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 022", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 023", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 024", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 025", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 026", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 027", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 028", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 029", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 030", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 031", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 032", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 033", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 034", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 035", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 036", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 037", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 038", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 039", 6, ["hydrate_retrieve"]),
    ("Placeholder: runway pad — fetch-needed seed 040", 6, ["hydrate_retrieve"]),
]


def build_seed_entries(need: int, used_ids: set[str]) -> list[QueueEntry]:
    seeds: list[QueueEntry] = []
    n = 1
    # First use curated named sources
    for title, tier, stages in SURVEY_SEED_SOURCES:
        if len(seeds) >= need:
            break
        sid = f"survey-seed-{n:03d}"
        while sid in used_ids:
            n += 1
            sid = f"survey-seed-{n:03d}"
        used_ids.add(sid)
        seeds.append(
            QueueEntry(
                id=sid,
                title_hint=title,
                status="seed_placeholder",
                priority_tier=tier,
                kedger_stages=stages,
                metric_impact=metric_impact_for(tier, "seed_placeholder"),
                refine_candidate=tier in {1, 2, 3, 4, 5},
                source_note="survey bibliography / CORPUS_INVENTORY §4 — needs fetch; NOT FULL",
            )
        )
        n += 1
    # Generic pads if curated list exhausted
    while len(seeds) < need:
        sid = f"survey-seed-{n:03d}"
        while sid in used_ids:
            n += 1
            sid = f"survey-seed-{n:03d}"
        used_ids.add(sid)
        tier = 6
        seeds.append(
            QueueEntry(
                id=sid,
                title_hint=f"Survey bibliography long-tail placeholder #{n:03d} (needs fetch)",
                status="seed_placeholder",
                priority_tier=tier,
                kedger_stages=["hydrate_retrieve"],
                metric_impact=metric_impact_for(tier, "seed_placeholder"),
                refine_candidate=False,
                source_note="padding slot from survey bibliographies — needs fetch; NOT FULL",
            )
        )
        n += 1
    return seeds


def build_queue() -> tuple[list[QueueEntry], dict[str, int]]:
    paths = iter_markdown_sources()
    id_hints = scan_arxiv_ids(paths)
    inv_text = INVENTORY.read_text(encoding="utf-8") if INVENTORY.exists() else ""
    full_map = load_full_from_inventory(inv_text)

    entries: list[QueueEntry] = []
    used: set[str] = set()

    # FULL ledger first (honest)
    for pid, meta in sorted(full_map.items(), key=lambda kv: kv[0]):
        title = meta["title"] or id_hints.get(pid, "")
        blob = f"{title} {meta.get('memo', '')}"
        tier = assign_tier(blob)
        stages = meta["stages"] or guess_stages(blob)
        entries.append(
            QueueEntry(
                id=pid,
                title_hint=title or id_hints.get(pid, ""),
                status="FULL",
                priority_tier=tier,
                kedger_stages=stages,
                metric_impact=metric_impact_for(tier, "FULL"),
                refine_candidate=is_refine_candidate(tier, "FULL", blob),
                source_note="CORPUS_INVENTORY §2 FULL ledger",
            )
        )
        used.add(pid)

    # Remaining scanned arXiv IDs → queued
    for pid in sorted(id_hints.keys()):
        if pid in used:
            # Enrich title if FULL row was thin
            continue
        title = id_hints[pid] or ""
        blob = title
        tier = assign_tier(blob if blob else pid)
        stages = guess_stages(blob)
        entries.append(
            QueueEntry(
                id=pid,
                title_hint=title or "(title TBD — queued for FULL deep-read)",
                status="queued",
                priority_tier=tier,
                kedger_stages=stages,
                metric_impact=metric_impact_for(tier, "queued"),
                refine_candidate=is_refine_candidate(tier, "queued", blob),
                source_note="scanned from docs/research/**/*.md + docs/*.md",
            )
        )
        used.add(pid)

    unique_arxiv = len(id_hints)
    full_count = sum(1 for e in entries if e.status == "FULL")

    target = 500
    if len(entries) < target:
        seeds = build_seed_entries(target - len(entries), used)
        entries.extend(seeds)

    # Stable prioritize: status FULL first within tier? Plan: prioritized queue —
    # queued/seed by tier asc, then FULL after or mixed. Prefer actionable queued first.
    def sort_key(e: QueueEntry):
        status_rank = {"queued": 0, "seed_placeholder": 1, "FULL": 2}.get(e.status, 9)
        return (e.priority_tier, status_rank, e.id)

    entries.sort(key=sort_key)

    stats = {
        "unique_arxiv_ids_found": unique_arxiv,
        "full_count": full_count,
        "queue_size": len(entries),
        "queued_count": sum(1 for e in entries if e.status == "queued"),
        "seed_placeholder_count": sum(1 for e in entries if e.status == "seed_placeholder"),
        "markdown_files_scanned": len(paths),
    }
    return entries, stats


def write_jsonl(entries: list[QueueEntry], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for e in entries:
            obj = {
                "id": e.id,
                "title_hint": e.title_hint,
                "status": e.status,
                "priority_tier": e.priority_tier,
                "kedger_stages": e.kedger_stages,
                "metric_impact": e.metric_impact,
                "refine_candidate": e.refine_candidate,
            }
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def write_markdown(entries: list[QueueEntry], stats: dict[str, int], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Kedger Track 0 — FULL deep-read queue (≥500)")
    lines.append("")
    lines.append("> **Program:** Kedger research (measure → refine).")
    lines.append("> **Honesty rule:** `FULL` only if listed in `CORPUS_INVENTORY.md` §2 ledger.")
    lines.append("> `seed_placeholder` entries need fetch — they are **not** FULL deep-reads.")
    lines.append("> Historical memos may say “MoDeX”; that is labeling debt, not product identity.")
    lines.append("")
    lines.append("## Stats")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|------:|")
    lines.append(f"| Unique arXiv IDs scanned | {stats['unique_arxiv_ids_found']} |")
    lines.append(f"| FULL (from inventory) | {stats['full_count']} |")
    lines.append(f"| queued (scanned, not FULL) | {stats['queued_count']} |")
    lines.append(f"| seed_placeholder (pad) | {stats['seed_placeholder_count']} |")
    lines.append(f"| **Queue size** | **{stats['queue_size']}** |")
    lines.append(f"| Markdown files scanned | {stats['markdown_files_scanned']} |")
    lines.append("")
    lines.append("## Priority tiers")
    lines.append("")
    lines.append("| Tier | Theme |")
    lines.append("|-----:|-------|")
    for t, label in TIER_LABELS.items():
        lines.append(f"| {t} | {label} |")
    lines.append("")
    lines.append("## Queue")
    lines.append("")
    lines.append("| # | ID | Title hint | Status | Tier | Kedger stages | Refine? |")
    lines.append("|--:|----|------------|--------|-----:|---------------|---------|")
    for i, e in enumerate(entries, 1):
        stages = ",".join(e.kedger_stages) if e.kedger_stages else "—"
        title = e.title_hint.replace("|", "\\|")
        lines.append(
            f"| {i} | `{e.id}` | {title} | {e.status} | {e.priority_tier} "
            f"({TIER_LABELS[e.priority_tier]}) | {stages} | "
            f"{'yes' if e.refine_candidate else 'no'} |"
        )
    lines.append("")
    lines.append("## Machine-readable")
    lines.append("")
    lines.append("- `docs/research/queue/full_queue.jsonl` — one JSON object per line.")
    lines.append("- Rebuild: `python3 scripts/research/build_full_queue.py`")
    lines.append("- Fetch arXiv HTML: `python3 scripts/research/fetch_paper.py <id>`")
    lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    entries, stats = build_queue()
    write_jsonl(entries, OUT_JSONL)
    write_markdown(entries, stats, OUT_MD)
    print(json.dumps(stats, indent=2))
    if stats["queue_size"] < 500:
        print("ERROR: queue size < 500", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
