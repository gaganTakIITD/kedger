"""Optional MCP adapter for Kedger read tools."""

from kedger.mcp.registry import TOOL_SPECS, call_tool, mcp_text_result
from kedger.mcp.server import serve

__all__ = ["TOOL_SPECS", "call_tool", "mcp_text_result", "serve"]
