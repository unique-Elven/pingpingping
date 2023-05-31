import threading
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar

from scapy_network import *


class Color:
    LINEN = '#FAF0E6'  # Linen 亚麻布
    GREY = '#D3D3D3'  # D3D3D3 LightGrey 浅灰色
    SILVER = '#C0C0C0'  # C0C0C0 Silver 银灰色
    BLACK = '#000000'  # 000000 Black 纯黑
    SNOW = '#FFFAFA'  # FFFAFA Snow 雪白色
    WHITE = '#FFFFFF'  # White 纯白色


class MyGui:
    def __init__(self, windows):
        self.windows = windows
        self.t = time.localtime()

    def set_windows(self):
        root.resizable(False, False)
        self.windows.config(bg=Color.SILVER)
        self.windows.title("PingPingPing")
        self.windows.geometry('500x350')
        self.pingE = Entry(root, font=('Times', 15))
        self.pingE.place(x=125, y=120, width=200, height=35)
        self.pingB = Button(root, text="Ping", font=("Times", 15), relief=RIDGE, command=self.ping_run)
        self.pingB.place(x=325, y=120, width=60, height=35)
        self.pingT = Text(root, font=('Times', 12))
        self.pingT.place(x=100, y=200, width=320, height=100)

    def ping_run(self):
        self.pingT.insert(END, f'正在Ping {self.pingE.get()}\n')
        self.pingT.update()
        state, loss = scapy_ping(self.pingE.get())
        if state:
            s = self.pingE.get() + f'连通！丢包率：{loss}\n'
        else:
            s = self.pingE.get() + f'无法连通！丢包率：{loss}\n'
        self.pingT.insert(END, s)

    def basic_background(self):
        pass

    def run(self):
        self.set_windows()
        self.windows.mainloop()


if __name__ == '__main__':
    root = Tk()
    gui = MyGui(root)
    gui.run()
