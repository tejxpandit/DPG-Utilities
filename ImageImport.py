# File      : Image Importer Class for DearPyGUI in Python
# Author    : Tej Pandit
# Date      : Oct 2024

import dearpygui.dearpygui as dpg
import numpy as np

class ImageImport:
    def __init__(self):
        self.image_type = "file"
        self.img_w = None
        self.img_h = None
        self.img_c = None
        self.img_d = None

    def setImageType(self, image_type):
        self.image_type = image_type
