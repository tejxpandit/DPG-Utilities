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
