cmake_minimum_required(VERSION 3.12)
project(Test)

set(CMAKE_CXX_STANDARD 11)

if (APPLE)
    add_definitions(-DGTEST_USE_OWN_TR1_TUPLE)
    add_definitions(-D__GLIBCXX__)
endif (APPLE)