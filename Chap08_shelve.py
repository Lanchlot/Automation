"""
一、shelve模块的使用
    ① shelve文件写入、读取的方法类似于字典
    ② 重复的键会覆盖shelve文件保存的数据
二、pyperclip模块的使用
    ① copy()方法
    ② paste()方法
"""
import shelve
import pyperclip


def save2shelve():
    cats = ['Zophie', 'Pooka', 'Simon']
    shelf_file = shelve.open('mydata')
    shelf_file['cats'] = cats
    shelf_file.close()


def read_from_shelve():
    shelf_file = shelve.open('mydata')
    print(shelf_file['cats'])
    print(type(shelf_file['cats']))
    shelf_file.close()


def save2clip():
    s = 'This is a string of words that want te be saved to clipboard'
    pyperclip.copy(s)


def read_from_clip():
    s = pyperclip.paste()
    print(s)


if __name__ == '__main__':
    read_from_clip()
