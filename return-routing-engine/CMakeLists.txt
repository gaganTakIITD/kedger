cmake_minimum_required(VERSION 3.16)
project(return_routing_engine CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(return_engine
    src/main.cpp
    src/engine.cpp
)

target_include_directories(return_engine PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
    ${CMAKE_CURRENT_SOURCE_DIR}/third_party
)

enable_testing()

add_executable(engine_tests
    tests/engine_tests.cpp
    src/engine.cpp
)

target_include_directories(engine_tests PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
    ${CMAKE_CURRENT_SOURCE_DIR}/third_party
)

add_test(NAME engine_tests COMMAND engine_tests)
