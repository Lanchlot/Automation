"""
遍历目录树深度优先算法
"""
import os
for foldername, subfolders, filenames in os.walk('.\\Test'):
    print('---------------------遍历分割符--------------------------------')
    print('The current folder is ：' + foldername)
    print('The subfolders in this folder :')
    for subfolder in subfolders:
        print(''.ljust(25) + subfolder)
    print('The file in this folder ：')
    for filename in filenames:
        print(''.ljust(25) + filename)
