# File      : Image Viewer Class for DearPyGUI in Python
# Author    : Tej Pandit
# Date      : Oct 2024

import dearpygui.dearpygui as dpg
from ImageImport import ImageImport

window_offset = 25

class ImageView:
    def __init__(self, parent=None, texture_registry=None, item_handler_registry=None):
        self.importer = ImageImport()
        self.parent = parent
        self.tex_reg_tag = texture_registry
        self.item_handler_reg_tag = item_handler_registry
        self.tex_tag = "image_tex"
        self.img_tag = "image_view"
        self.img_width = None
        self.img_height = None
        self.img_channels = None
        self.img_data = None
        self.img_scale = 1.0
        self.initTextureRegistry()
        self.initItemHandlerRegistry()
        self.initAutoResize()

    # Initialize Texture Registry
    def initTextureRegistry(self):
        if self.tex_reg_tag is None:
            self.tex_reg_tag = dpg.add_texture_registry(show=False)
