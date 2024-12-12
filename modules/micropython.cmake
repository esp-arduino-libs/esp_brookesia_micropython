# This top-level micropython.cmake is responsible for listing
# the individual modules we want to include.
# Paths are absolute, and ${CMAKE_CURRENT_LIST_DIR} can be
# used to prefix subdirectories.

include(${CMAKE_CURRENT_LIST_DIR}/lv_binding_micropython/micropython.cmake)

if(ESP_PLATFORM)
    include(${CMAKE_CURRENT_LIST_DIR}/esp-lib-utils/micropython.cmake)
    include(${CMAKE_CURRENT_LIST_DIR}/ESP32_IO_Expander/micropython.cmake)
    include(${CMAKE_CURRENT_LIST_DIR}/ESP32_Display_Panel/micropython.cmake)
endif()
