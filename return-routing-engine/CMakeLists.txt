cmake_minimum_required(VERSION 3.16)
project(return_routing_engine LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  json
  URL https://github.com/nlohmann/json/releases/download/v3.11.3/json.tar.xz
)
FetchContent_MakeAvailable(json)

add_executable(return_router
  src/main.cpp
  src/engine.cpp
)
target_include_directories(return_router PRIVATE include)
target_link_libraries(return_router PRIVATE nlohmann_json::nlohmann_json)

enable_testing()
add_test(NAME route_sample
  COMMAND return_router ${CMAKE_SOURCE_DIR}/data
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)
