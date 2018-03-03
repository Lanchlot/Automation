"""
使用logging模块来调试程序:
    在basicConfig函数里可以调整日志输入的级别，当前为DEBUG及以上
    在basicConfig函数里加上参数filename参数可以将日志写入到文本文件，控制台不再显示。写入方式为追加

"""
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program')
logging.info('Start of the program')
logging.warning('Start of the program')
logging.error('Start of the program')
logging.critical('Start of the program')

