"""
zipfile模块
    读取
        ZipInfo对象
        getinfo('spam.txt')
        getinfo('spam.txt').file_size
        getinfo('spam.txt').compress_size
    解压
        extract()       解压单个文件。如果解压压缩文件中的文件夹，解压出来的文件夹为空
        extractall()    解压全部
    写入
        创建ZipFile对象时，增加参数'w'
        ZipFile().write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
"""

import zipfile
examplezip = zipfile.ZipFile('F:\\PyCharmProjects\\Automation\\Test\\example.zip')

# read
print(examplezip.namelist())
spaminfo = examplezip.getinfo('spam.txt')
print(spaminfo.file_size)
print(spaminfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spaminfo.file_size / spaminfo.compress_size, 2)))

# uncompress
examplezip.extractall('F:\\PyCharmProjects\\Automation\\Test\\example')
examplezip.extract('spam.txt', '.\\Test')
examplezip.close()

# create and add to zip
newzip = zipfile.ZipFile('.\\Test\\newzip.zip', 'w')
newzip.write('.\\Test\\spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newzip.close()
