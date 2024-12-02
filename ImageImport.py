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
    
    def OPENCV_loader(self, image):
        # Extract image dimensions
        w, h, c = self.extractDimensions(image)
        # Convert BGR to RGB
        frame = np.flip(image, 2)
        # Flatten N-Dim to 1-Dim Structure
        frame = frame.ravel()
        # Change Data Type to float32
        frame = np.asarray(frame, dtype='f')
        # Normalize Texture Data
        tex_data = np.true_divide(frame, 255.0)
        return w, h, c, tex_data

    def MATPLOTLIB_loader(self, image):
        return None
    
    def extractDimensions(self, image):
        n = np.ndim(image)
        d = np.shape(image)
        w = h = c = 1
        if n == 1:
            w = d[0]
        elif n == 2:
            w = d[0]
            h = d[1]
        else:
            w = d[0]
            h = d[1]
            c = d[2]
        return w, h, c
    
