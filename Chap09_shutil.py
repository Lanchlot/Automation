"""
一、 shutil模块
    ① copy()      只能复制文件，若文件已经存在则会覆盖
    ② copytree()  复制、子文件、子文件夹、子文件夹里的文件。 目标文件夹已存在会报错
    ③ move()      移动单个文件、文件夹到目标文件夹，可以重命名。目标文件夹若不存在会报错。
"""
import shutil
shutil.copytree('D:\\MiCloud\\Pictures', 'F:\\PyCharmProjects\\Automation\\Test\\Pictures')


