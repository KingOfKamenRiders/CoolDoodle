from tkinter import *
from ui.menu_bar import MenuWrapper
from ui.side_info import SideInfo
from ui.canvas_wrapper import CanvasWrapper


class App:
    """
    该类是前端界面的top-level类，包含了所有的ui控件
    """
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        main = Frame()
        main.pack(side='left')
        my_canvas = CanvasWrapper(main)
        MenuWrapper(self.root, my_canvas)
        side = Frame(bd=5, relief='groove')
        side.pack(side='right')
        side_info = SideInfo(side)
        my_canvas.set_side_info(side_info)
        side_info.set_c_wrapper(my_canvas)