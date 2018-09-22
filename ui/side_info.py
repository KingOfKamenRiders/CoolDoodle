from tkinter import *
from tkinter.ttk import Separator, Button


class SideInfo:
    """
    该类是侧边信息栏的包装类，负责展示涂鸦信息和增加tag
    """
    def __init__(self, master):
        # data binding
        self.display_id = StringVar()
        self.display_shape = StringVar()
        self.display_tag = StringVar()
        # components
        self.doodle_list = Listbox(master)
        self.doodle_list.grid(row=5, column=1)
        self.doodle_list.bind('<<ListboxSelect>>', self.handle_select)
        self.c_wrapper = None
        self.startButton = Button(master, text='开始绘制', command=self.handle_start).grid(row=0)
        self.finishButton = Button(master, text='结束绘制',command=self.handle_finish).grid(row=0,column=1)
        Label(master, text='id:').grid(row=1)
        Entry(master,textvariable=self.display_id, state=DISABLED).grid(row=1, column=1)
        Label(master, text='识别:').grid(row=2)
        Entry(master, textvariable=self.display_shape, state=DISABLED).grid(row=2, column=1)
        Label(master, text='标签:').grid(row=3)
        self.tag_input = Entry(master, textvariable=self.display_tag)
        self.tag_input.grid(row=3, column=1)
        self.tag_input.bind('<Return>', self.handle_tag)
        self.tag_input.bind('<FocusOut>', self.handle_tag)
        Separator(master, orient='horizontal').grid(row=4)

    def insert(self, index, s):
        """
        向涂鸦list中新增加一条记录
        :param index:
        :param s:
        :return:
        """
        self.doodle_list.insert(index,s)

    def set_c_wrapper(self, c):
        self.c_wrapper = c

    def handle_start(self):
        """
        开始按钮的响应方法，通知画布组件开始记录轨迹
        :return:
        """
        self.c_wrapper.start_paint()

    def handle_finish(self):
        """
        结束按钮的响应方法，通知画布组件结束本次涂鸦
        :return:
        """
        self.c_wrapper.finish_paint()

    def handle_select(self, *args):
        """
        当用户选择涂鸦list中的条目后，面板展示对应涂鸦的信息
        :param args:
        :return:
        """
        index = self.doodle_list.curselection()[0]
        info = self.doodle_list.get(index)
        self.display_id.set(info.split('-')[0])
        self.display_shape.set(info.split('-')[1])
        self.display_tag.set(self.c_wrapper.get_tag(self.display_id.get()))
        self.c_wrapper.highlight(info.split('-')[0])

    def handle_tag(self, *args):
        """
        该方法用于保存用户的tag
        :param args:
        :return:
        """
        print(self.display_id.get())
        print(self.display_tag.get())
        self.c_wrapper.set_tag(self.display_id.get(), self.display_tag.get())


