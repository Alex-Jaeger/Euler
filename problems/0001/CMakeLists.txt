cmake_minimum_required(VERSION 3.10)

project(euler_problem_0001 CXX)

set(euler_problem_0001_library_deps          PARENT_SCOPE)

add_library(
    ${PROJECT_NAME}
    problem_0001.cpp
)
