cmake_minimum_required(VERSION 3.8)
project(alan_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/RectangleArea.srv"
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_lint_cmake_copyright_FOUND TRUE)
  set(ament_lint_cmake_baseline_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
