import lvgl as lv
import lv_utils
from display_driver_utils import driver

if __name__ == '__main__':
    print('Running main.py')

    print('Initializing lvgl')
    lv.init()

    print('Initializing driver')
    drv = driver(320, 240)
