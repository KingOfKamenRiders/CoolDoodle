from tkinter import Menu,filedialog
from bl.doodle_service import DoodleServiceIMP


class MenuWrapper:
    """
    该类是菜单组件的wrapper类，负责文件的读取&保存
    """
    def __init__(self, master, c_wrapper):
        self.doodle_service = DoodleServiceIMP()
        self.c_wrapper = c_wrapper
        menu = Menu()
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label='打开',command=self.open_file)
        filemenu.add_command(label='保存',command=self.save_file)
        menu.add_cascade(menu=filemenu, label='文件')
        master.config(menu=menu)

    def open_file(self):
        doodles = self.doodle_service.get_doodle()
        if doodles is None:
            return
        self.c_wrapper.set_doodles(doodles)

    def save_file(self):
        self.doodle_service.save_doodle(self.c_wrapper.doodles)


