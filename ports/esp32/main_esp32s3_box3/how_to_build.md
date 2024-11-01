## How to Build

```bash
make BOARD=ESP32_S3_BOX_3 MAIN_VARIANT=box3 USER_C_MODULES=../../../modules/micropython.cmake PORT=/dev/ttyACM0 -C ports/esp32 deploy
```
