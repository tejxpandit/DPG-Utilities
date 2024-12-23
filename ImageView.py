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

    # Optional : Change Custom/Existing Texture Registry
    def setTextureRegistry(self, texture_registry_tag):
        self.tex_reg_tag = texture_registry_tag

    # Initialize Item Handler Registry
    def initItemHandlerRegistry(self):
        if self.item_handler_reg_tag is None:
            self.item_handler_reg_tag = dpg.add_item_handler_registry(show=False)
        
    # Initialize Auto-Resize
    def initAutoResize(self):
        dpg.add_item_resize_handler(parent=self.item_handler_reg_tag, callback=self.autoRescale)
        dpg.bind_item_handler_registry(self.parent, self.item_handler_reg_tag)

    # Set ImageView Parent Container
    def setParent(self, parent):
        self.parent = parent

    # Set Image Scale
    def setImageScale(self, scale):
        self.img_scale = scale

    # Set Image Max Width
    def setImageWidth(self, width):
        self.img_scale = width / self.img_width

    # Set Image Max Height
    def setImageHeight(self, height):
        self.img_scale = height / self.img_height

    # Auto-Rescale
    def autoRescale(self):
        if self.parent is not None:
            win_width = dpg.get_item_width(self.parent)
            win_height = dpg.get_item_height(self.parent)
            self.setImageWidth(win_width-window_offset)
            dpg.configure_item(self.img_tag, width=self.img_width*self.img_scale, height=self.img_height*self.img_scale)
            print(win_width, win_height)
            print(self.img_scale)

    # IMP : Set Image Type
    def setImageType(self, image_type):
        self.importer.setImageType(image_type)

    # Create New Image
    def newImage(self, image):
        # Import Image Data
        self.importer.imageConvert(image)
        # Get Image Data
        self.img_width, self.img_height, self.img_channels, self.img_data = self.importer.getImage()
        # Add Image Texture to Registry
        # self.tex_tag = dpg.add_static_texture(width=self.img_width, height=self.img_height, default_value=self.img_data, parent=self.tex_reg_tag)
        self.tex_tag = dpg.add_raw_texture(width=self.img_width, height=self.img_height, default_value=self.img_data, format=dpg.mvFormat_Float_rgba, parent=self.tex_reg_tag)
        # Add Image to Parent Container
        self.img_tag = dpg.add_image(texture_tag=self.tex_tag, parent=self.parent, width=self.img_width*self.img_scale, height=self.img_height*self.img_scale)

    # View Image
    def viewImage(self):
        # Add Image to Parent Container
        self.img_tag = dpg.add_image(texture_tag=self.tex_tag, parent=self.parent, width=self.img_width*self.img_scale, height=self.img_height*self.img_scale)

    # Update Image
    def updateImage(self, image):
        # Import Image Data
        self.importer.imageConvert(image)
        # Get Image Data
        self.img_width, self.img_height, self.img_channels, self.img_data = self.importer.getImage()
        # Update Image Data
        dpg.set_value(self.tex_tag, self.img_data)

    # TODO : Delete Image Textures
    # TODO : Create Empty Image Placeholder
    # TODO : Delete previous Image Tex Tag if it exists
    # TODO : Based on No. of Channels, choose correct format RGB/RGBA
    # TODO : Allow for non-window based parents
    # TODO : Enable and disable for autorescale
    # TODO : Separate base-scale and auto-scale variables

#----------------
# EXAMPLE : USAGE
if __name__ == '__main__': 
    # DPG Context
    dpg.create_context()
    # DPG Viewport
    dpg.create_viewport(title="Image Viewer", width=600, height=300)
    # DPG Window
    dpg.add_window(label="Image Viewer", tag="img_view")
    dpg.add_group(parent="img_view", tag="main_group")

    # DPG Image Viewer Example
    ImgViewer = ImageView("main_group")
    ImgViewer.newImage("data/TestImage.png")

    # DPG Render Context
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
    