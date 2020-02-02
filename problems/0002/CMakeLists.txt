cmake_minimum_required(VERSION 3.10)

set(PROBLEM_NUMBER 0002)
project(euler_problem_${PROBLEM_NUMBER} CXX)

set(${PROJECT_NAME}_library_deps          PARENT_SCOPE)

add_library(
    ${PROJECT_NAME}
    problem_${PROBLEM_NUMBER}.cpp
)
