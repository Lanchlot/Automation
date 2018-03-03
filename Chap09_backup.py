"""
文件备份系统：
    一、因为备份的压缩文件不在需要备份的文件夹中，所以在写入压缩文件时，不用检查是不是压缩文件
    二、如果程序和需要备份的文件夹不在同一目录下，在生成的备份压缩文件中会存在多余路径
"""

import zipfile
import os


def backup2zip(folder):
    number = 1
    while True:
        backupzipname = folder + '_' + str(number) + '.zip'
        if not os.path.exists(backupzipname):
            break
        number += 1
    backupzip = zipfile.ZipFile(backupzipname, 'w')
    for foldername, subfolders, files in os.walk(folder):
        for file in files:
            print('Add ' + foldername + '\\' + file)
            backupzip.write(os.path.join(foldername, file), compress_type=zipfile.ZIP_DEFLATED)
    backupzip.close()


if __name__ == '__main__':
    backup2zip('.\\Test\\example')

