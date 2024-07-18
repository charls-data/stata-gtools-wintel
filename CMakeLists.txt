cmake_minimum_required(VERSION 3.15)
project(stata-gtools-wintel)

# check intel complier
if (NOT CMAKE_C_COMPILER_ID STREQUAL "IntelLLVM")
    message(FATAL_ERROR "This project requires the Intel icx compiler.")
endif()

# openmp
option(USE_OPENMP "Use OpenMP" OFF)

# build type
if (NOT DEFINED CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE RELEASE cache string "Build Type")
endif ()

# set complier flags
set(CMAKE_C_FLAGS "/W1 /nologo /MD")
if (USE_OPENMP)
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /Qopenmp")
  add_compile_definitions(GTOOLSOMP)
endif ()
set(CMAKE_C_FLAGS_RELEASE "/Ox /QxHost /DNDEBUG")
add_compile_options(/wd4996)

include_directories(${PROJECT_SOURCE_DIR}/stata-gtools/lib/spookyhash/src)

set(SOURCE_FILES
    ${PROJECT_SOURCE_DIR}/stata-gtools/src/plugin/gtools.c
    ${PROJECT_SOURCE_DIR}/stata-gtools/src/plugin/spi/stplugin.c
    ${PROJECT_SOURCE_DIR}/stata-gtools/lib/spookyhash/src/context.c
    ${PROJECT_SOURCE_DIR}/stata-gtools/lib/spookyhash/src/globals.c
    ${PROJECT_SOURCE_DIR}/stata-gtools/lib/spookyhash/src/spookyhash.c
)

add_library(gtools SHARED ${SOURCE_FILES})
set_target_properties(gtools PROPERTIES
    OUTPUT_NAME "gtools_windows_v3.plugin"
    SUFFIX ""
    PREFIX ""
)
