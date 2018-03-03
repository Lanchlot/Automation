"""
一、os模块
    ① getcwd()
    ② chdir()
    ③ makedirs()
    ④ listdir()     只会返回指定目录下的文件和目录，单层
二、 os.path模块
    ① os.path.abspath()
    ② os.path.isabs()
    ③ os.path.relpath(path, start)
    ④ os.path.dirname()
    ⑤ os.path.basename()
    ⑥ os.path.split()   返回(dirname(), basename())的元组
    ⑦ os.path.getsize() 返回单个文件的大小
    ⑧ os.path.isdir     是不是目录
    ⑨ os.path.isfile()  是不是文件
    ⑩ os.path.exists()
"""
import os
# 获取当前工作目录、切换当前工作目录、新建文件夹
print(os.getcwd())
os.chdir('F:\\PyCharmProjects')
print(os.getcwd())
os.chdir('F:\\PyCharmProjects\\Automation')
print(os.getcwd())
print(os.path.relpath('F:\\Kindle'))

# 最后一个反斜杠之前、之后的内容
print(os.path.dirname('C:\\Users\\Administrator\\Desktop'))
print(os.path.basename('C:\\Users\\Administrator\\Desktop'))

# 查看文件大小、文件夹内容
print(os.listdir('F:\\PyCharmProjects'))
print(os.path.getsize('E:\\Softwares\\iCloudSetup.exe'))

# 检查路径有效性
print(os.path.isdir('E:\\Softwares\\iCloudSetup.exe'))
print(os.path.isfile('E:\\Softwares\\iCloudSetup.exe'))

#


