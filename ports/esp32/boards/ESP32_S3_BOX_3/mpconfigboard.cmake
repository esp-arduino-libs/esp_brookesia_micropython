set(IDF_TARGET esp32s3)

set(SDKCONFIG_DEFAULTS
    ${SDKCONFIG_IDF_VERSION_SPECIFIC}
    boards/sdkconfig.usb
    boards/sdkconfig.ble
    boards/ESP32_S3_BOX_3/sdkconfig.base
    boards/ESP32_S3_BOX_3/sdkconfig.board
)
