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

    def imageConvert(self, image, img_type="file"):
        self.image_type = img_type
        if self.image_type == "file":
            self.img_w, self.img_h, self.img_c, self.img_d = dpg.load_image(image)
        elif self.image_type == "pil":
            self.img_w, self.img_h, self.img_c, self.img_d = self.PIL_loader(image)
        elif self.image_type == 'opencv':
            self.img_w, self.img_h, self.img_c, self.img_d = self.OPENCV_loader(image)
        elif self.image_type == 'matplotlib':
            self.img_w, self.img_h, self.img_c, self.img_d = self.MATPLOTLIB_loader(image)
        
    def getImage(self):
        return self.img_w, self.img_h, self.img_c, self.img_d

    def PIL_loader(self, image):
        return None
    def MATPLOTLIB_loader(self, image):
        return None
