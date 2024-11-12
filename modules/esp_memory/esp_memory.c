#include "string.h"
#include "esp_heap_caps.h"
#include "py/runtime.h"

static mp_obj_t esp_memory_print_summary(void) {
    char buffer[128];
    sprintf(buffer,
            "         Biggest  /     Free /    Total\n"
            " SRAM : [%8d / %8d / %8d]\n"
            "PSRAM : [%8d / %8d / %8d]",
            (int)heap_caps_get_largest_free_block(MALLOC_CAP_INTERNAL),
            (int)heap_caps_get_free_size(MALLOC_CAP_INTERNAL),
            (int)heap_caps_get_total_size(MALLOC_CAP_INTERNAL),
            (int)heap_caps_get_largest_free_block(MALLOC_CAP_SPIRAM),
            (int)heap_caps_get_free_size(MALLOC_CAP_SPIRAM),
            (int)heap_caps_get_total_size(MALLOC_CAP_SPIRAM));
    printf("%s\n", buffer);

    return mp_const_none;
}
static MP_DEFINE_CONST_FUN_OBJ_0(esp_memory_print_summary_obj, esp_memory_print_summary);

static const mp_rom_map_elem_t esp_memory_module_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_esp_memory) },
    { MP_ROM_QSTR(MP_QSTR_print_summary), MP_ROM_PTR(&esp_memory_print_summary_obj) },
};
static MP_DEFINE_CONST_DICT(esp_memory_module_globals, esp_memory_module_globals_table);

// Define module object.
const mp_obj_module_t esp_memory_module = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t *)&esp_memory_module_globals,
};

// Register the module to make it available in Python.
MP_REGISTER_MODULE(MP_QSTR_esp_memory, esp_memory_module);
