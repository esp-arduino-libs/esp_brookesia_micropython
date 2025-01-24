import micropython as mpy
import esp_utils as utils
import esp_panel as panel
import gc

for i in range(100):
    mpy.mem_info()
    utils.mem_info()

    b = panel.Board()

    b.begin()
    b.color_bar_test()
    b.deinit()

    utils.mem_info()

    gc.collect()
    mpy.mem_info()
    utils.mem_info()

gc.collect()
mpy.mem_info()
utils.mem_info()
