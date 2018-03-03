import subprocess


def process_open():
    """打开外部程序，无参数"""
    calculate = subprocess.Popen(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    print(calculate.poll())     # 外部程序未执行完毕打印None, 执行完毕打印进程的整数退出代码
    calculate.wait()            # 在调用的外部程序执行完毕之前，阻塞程序
    print('程序已经执行完毕！')
    print(calculate.poll())


def process_open_args():
    """打开外部程序，有参数.参数为唯一的列表"""
    subprocess.Popen([r'C:\Program Files\Mozilla Firefox\firefox.exe', 'www.swufe.edu.cn'])


def python_open():
    """打开python脚本"""
    python_process = subprocess.Popen([r'F:\PyCharmProjects\Automation\venv\Scripts\python.exe', r'F:\hello.py'])
    python_process.wait()


def open_with_default_process():
    """使用系统默认的程序打开文件"""
    subprocess.Popen(['start', r'F:\hello.txt'], shell=True)


if __name__ == '__main__':
    subprocess.Popen([r'E:\Program Files\Thunder\Program\Thunder.exe',
                      r'ftp://ygdy8:ygdy8@yg72.dydytt.net:8160/阳光电影www.ygdy8.com.引爆者.HD.1080p.国语中字.mkv'])
