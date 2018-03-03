import logging
import traceback
import PyPDF2.utils
# 在控制台输出日志，方便调试
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# pdf文件为Test文件夹下economist.pdf
file = open('Test\\economist.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(file)
logging.debug('文件共{}页'.format(pdfreader.numPages))

# 对于pdf文件的每一页，提取文本内容后，写入economist.txt
for pagenum in range(1, pdfreader.numPages):
    logging.debug('开始处理第{}页'.format(pagenum))
    try:
        page = pdfreader.getPage(pagenum)
        text = page.extractText()
        logging.debug('第{}页内容已提取'.format(pagenum+1))
        with open('Test\\economist.txt', 'a', encoding='utf-8') as f:
            f.write(text)
        logging.debug('第{}页内容已经写入文本文档'.format(pagenum+1))

        # 异常处理，将异常回溯信息写入traceback.txt文件
    except PyPDF2.utils.PdfStreamError as e:
        logging.warning('第{}页，异常'.format(pagenum+1))
        with open('Test\\traceback.txt', 'a') as f:
            f.write(traceback.format_exc())
file.close()
