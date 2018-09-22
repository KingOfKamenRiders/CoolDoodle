from tkinter import Canvas,END
from entity.doodle import Doodle
from bl.analysis_service import AnalyzeServiceIMP
import copy


class CanvasWrapper:
    """
    该类是画布的wrapper类，包含画布组件的操作，并且保存了当前画布上的数据
    """
    doodle_id = 1
    analyze_service = AnalyzeServiceIMP()

    def __init__(self, master):
        self.side_info = None
        self.c = Canvas(master, width=700, height=500, cursor='pencil', relief='groove', bd=5)
        self.c.pack()
        self.prev = None
        self.doodles = []
        self.lines = []
        self.segments = []

    def set_side_info(self, s):
        self.side_info = s

    def handle_mouse_click(self, e):
        self.lines.append(copy.deepcopy(self.segments))
        self.segments = []
        self.prev = e

    @staticmethod
    def distance_between(a,b):
        return ((a.x-b.x)**2+(a.y-b.y)**2)**.5

    def handle_mouse_move(self, e):
        if self.distance_between(e,self.prev) > 5:
            self.c.create_line(self.prev.x, self.prev.y, e.x, e.y, width=2, tags='doodle'+str(self.doodle_id))
            self.segments.append(e.x)
            self.segments.append(e.y)
            self.prev = e

    def start_paint(self):
        """
        开始记录画笔的轨迹
        :return:
        """
        self.c.bind('<Button-1>', self.handle_mouse_click)
        self.c.bind('<B1-Motion>', self.handle_mouse_move)
        self.lines = []
        self.segments = []
        pass

    def finish_paint(self):
        """
        结束一次涂鸦，将记录的轨迹用于生成一个Doodle类对象，并进行形状分析
        :return:
        """
        self.c.unbind('<Button-1>')
        self.c.unbind('<B1-Motion>')
        d = Doodle(self.doodle_id)
        self.doodle_id = self.doodle_id+1
        self.lines.append(copy.deepcopy(self.segments))
        d.lines = copy.deepcopy(self.lines)
        d.shape = self.analyze_service.analyze_shape(d)
        self.c.create_text(self.lines[-1][-2],self.lines[-1][-1], text=str(d.shape),tags='doodle'+str(d.id))
        self.doodles.append(d)
        self.side_info.insert(END, str(d.id)+'-'+str(d.shape))
        pass

    def set_tag(self, did=0, tag=''):
        for doodle in self.doodles:
            if doodle.id == int(did):
                doodle.tag = tag

    def get_tag(self, did=0, tag=''):
        for doodle in self.doodles:
            if doodle.id == int(did):
                return doodle.tag
        return ''

    def set_doodles(self, doodles):
        """
        读取Doodle类的信息重新绘制到画布上
        :param doodles:
        :return:
        """
        self.doodles = copy.deepcopy(doodles)
        self.doodle_id = doodles[-1].id+1
        for doodle in self.doodles:
            for line in doodle.lines:
                if len(line) >= 4:
                    prev_x = line[0]
                    prev_y = line[1]
                    i = 2
                    while i < len(line):
                        self.c.create_line(prev_x,prev_y,line[i],line[i+1], width=2, tags='doodle'+str(doodle.id))
                        prev_x = line[i]
                        prev_y = line[i+1]
                        i += 2
            self.side_info.insert(END, str(doodle.id) + '-' + str(doodle.shape))
            self.c.create_text(doodle.lines[-1][-2],doodle.lines[-1][-1],text=str(doodle.shape),tags='doodle'+str(doodle.id))

    def highlight(self, tag):
        """
        对选中的涂鸦设置高亮显示
        :param tag:
        :return:
        """
        for i in range(1, self.doodle_id+1):
            if str(i) == tag:
                self.c.itemconfigure('doodle'+str(i), fill='blue')
            else:
                self.c.itemconfigure('doodle'+str(i), fill='black')

