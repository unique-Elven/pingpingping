import threading
from tkinter import *
from tkinter import messagebox


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

    def set_windows(self):
        root.resizable(False, False)
        self.windows.config(bg=Color.WHITE)
        self.windows.title("PingPingPing")
        self.windows.geometry('500x350')
        self.pingE = Entry(root, font=('Times', 15))
        self.pingE.place(x=125, y=120, width=200, height=35)
        self.pingB = Button(root, text="Ping", font=("Times", 15), bg='#DDDDDD')
        self.pingB.place(x=325, y=120, width=60, height=35)

    def basic_background(self):
        pass

    def run(self):
        self.set_windows()
        self.windows.mainloop()


if __name__ == '__main__':
    root = Tk()
    gui = MyGui(root)
    gui.run()
