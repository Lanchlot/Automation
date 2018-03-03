"""
GUI程序：
    step1 用户选择目录
    step2 用户选择文件扩展名
    step3 显示对应的文件
    step4 当用户双击文件名时，在另一个窗口打开文件
"""
from tkinter import *
from tkinter import scrolledtext
import os
from tkinter import filedialog


# <------功能函数-------->
def callback_1():
    directory = filedialog.askdirectory()
    dir_v.set(directory)


def callback_2():
    path = os.path.abspath(dir_v.get())
    suffix = filetype.get()
    filetext.delete(1.0, END)
    for folder, subfolders, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                filetext.insert(INSERT, os.path.join(folder, file) + '\n')


# <------设计界面------>
top = Tk()
top.title('文件查找窗口')
dir_v = StringVar()
dir_v.set('当前未选择路径')
# 第一行选择文件目录
Label(top, text='请选择文件目录：').grid(row=0, column=0, padx=10, pady=10)
Entry(top, width=30, textvariable=dir_v).grid(row=0, column=1, padx=10, pady=10)
Button(top, text='请选择路径...', command=callback_1).grid(row=0, column=2, padx=10, pady=10)
# 第二行选择文件类型
Label(top, text='请选择文件类型：').grid(row=1, column=0, padx=10, pady=10)
filetype = Spinbox(top, width=30, values=('.txt', '.py', '.zip', '.pdf', '.csv', '.doc', '.ppt', '.jpg'))
filetype.grid(row=1, column=1, padx=10, pady=10)
Button(top, text='确定', width=10, command=callback_2).grid(row=1, column=2, padx=10, pady=10)
# 第三行文本框用于显示文件名
filetext = scrolledtext.ScrolledText(top, height=20, width=80)
filetext.grid(row=2, columnspan=3)
mainloop()
