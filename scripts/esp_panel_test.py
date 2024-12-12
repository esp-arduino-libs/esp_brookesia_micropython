import micropython as mpy
import esp_utils as utils
import esp_panel as panel
import gc

mpy.mem_info()
utils.mem_info()

b = panel.Board()

b.init()
b.begin()
b.color_bar_test()
b.deinit()

gc.collect()
mpy.mem_info()
utils.mem_info()
