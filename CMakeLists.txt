cmake_minimum_required(VERSION 3.10)

project(project_euler CXX)

# ---------------------------------------------

add_subdirectory(problems/)



# ---------------------------------------------

set(EULER_PROBLEM_NUMBER 0028)

configure_file(
    ${CMAKE_SOURCE_DIR}/runner/main.cpp.in
    ${CMAKE_BINARY_DIR}/main.cpp
)

add_executable(
    ${CMAKE_PROJECT_NAME}
    ${CMAKE_BINARY_DIR}/main.cpp
)

set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES LINKER_LANGUAGE CXX)

target_include_directories(
    ${CMAKE_PROJECT_NAME}
    PUBLIC
        ${CMAKE_SOURCE_DIR}/problems/
)

target_link_libraries(
    ${CMAKE_PROJECT_NAME}
    PUBLIC
        euler_problem_${EULER_PROBLEM_NUMBER}
)
