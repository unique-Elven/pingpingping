import threading
from tkinter import *
from tkinter import messagebox


class Color:
    # 自定义颜色
    ACHIEVEMENT = (220, 160, 87)
    VERSION = (220, 160, 87)
    # 固定颜色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)  # 中性灰
    TRANSPARENT = (255, 255, 255, 0)  # 白色的完全透明


class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg='#CCCCCC')
        self.root.title("PingPingPing")
        self.root.geometry('350x220')

    def basic_background(self):
        pass

    def mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    game = Interface()
    game.mainloop()
