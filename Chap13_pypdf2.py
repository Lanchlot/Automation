import PyPDF2
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_from_pdf():
    """路径为：只读、二进制File对象 --> PdfFileReader对象 --> 获取页面Page --> page.extractText()方法返回字符串"""
    pdfobj = open('Test\\meetingminutes.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdfobj)
    print(pdfreader.numPages)
    page0 = pdfreader.getPage(11)
    text = page0.extractText()
    print(text)


def decrypt_pdf():
    """解密方法：pdfreader.decrypt('password')"""
    pdfreader = PyPDF2.PdfFileReader(open('Test\\encrypted.pdf', 'rb'))
    print('是否加密：', pdfreader.isEncrypted)
    pdfreader.decrypt('rosebud')
    page0 = pdfreader.getPage(0)
    text0 = page0.extractText()
    print(text0)


def create_paf():
    """只允许从其他pdf页面中拷贝、旋转、重叠、加密。不允许直接编辑pdf文件"""
    pass


def copy_page():
    """路径为：PdfFileWriter对象 --> addPage(Page)方法 --> File对象wb --> PdfFileWriter.write(File)"""
    pdffile1 = open('Test\\meetingminutes.pdf', 'rb')
    pdffile2 = open('Test\\meetingminutes2.pdf', 'rb')
    pdfreader1 = PyPDF2.PdfFileReader(pdffile1)
    pdfreader2 = PyPDF2.PdfFileReader(pdffile2)
    pdfwriter = PyPDF2.PdfFileWriter()
    for pagenum in range(pdfreader1.numPages):
        page = pdfreader1.getPage(pagenum)
        pdfwriter.addPage(page)
        logging.debug('第一份文件第{}页已经写入' .format(pagenum))
    for pagenum in range(pdfreader2.numPages):
        page = pdfreader2.getPage(pagenum)
        pdfwriter.addPage(page)
        logging.debug('第二份文件第{}页已经写入'.format(pagenum))
    pdfoutputfile = open('Test\\combinedminutes.pdf', 'wb')
    pdfwriter.write(pdfoutputfile)
    pdfoutputfile.close()


def rotate_page():
    """Page.rotateClockwise(90/180/270), Page.rotateCounterClockwise(90/180/270)"""
    pdffile = open('Test\\meetingminutes.pdf', 'rb')
    pdfoutputfile = open('Test\\rotatedmeetingminutes.pdf', 'wb')
    pdfreader = PyPDF2.PdfFileReader(pdffile)
    pdfwriter = PyPDF2.PdfFileWriter()
    page0 = pdfreader.getPage(0)
    page1 = pdfreader.getPage(1)
    pdfwriter.addPage(page0.rotateClockwise(90))
    pdfwriter.addPage(page1.rotateCounterClockwise(90))
    pdfwriter.write(pdfoutputfile)
    pdffile.close()
    pdfoutputfile.close()
    logging.debug(msg='页面已经旋转并写入')


def merge_page():
    """page1.mergePage(page2)方法并不返回新页面，而是直接改变page1的内容"""
    minutesfile = open('Test\\meetingminutes.pdf', 'rb')
    watermarkfile = open('Test\\watermark.pdf', 'rb')
    watermarkreader = PyPDF2.PdfFileReader(watermarkfile)
    minutesreader = PyPDF2.PdfFileReader(minutesfile)
    pdfwriter = PyPDF2.PdfFileWriter()
    for pagenum in range(minutesreader.numPages):
        page = minutesreader.getPage(pagenum)
        page.mergePage(watermarkreader.getPage(0))      # page1.mergePage(page2)方法并不返回新页面，而是直接改变page1的内容
        pdfwriter.addPage(page)
        logging.debug(msg='第%d页已经写入' % pagenum)
    pdfoutputfile = open('Test\\meetingminutes_watermark.pdf', 'wb')
    pdfwriter.write(pdfoutputfile)
    minutesfile.close()
    watermarkfile.close()
    pdfoutputfile.close()
    logging.debug(msg='水印文件已经创建!')


def encrypt_page():
    """PdfFileWriter.encrypt('password1', 'password2')"""
    pass


if __name__ == '__main__':
        merge_page()
