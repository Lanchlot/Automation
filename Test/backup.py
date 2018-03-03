"""
程序和需要备份的文件夹在同一文件夹下，所以不会存在多余的路径
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
    backup2zip('.\\example')

