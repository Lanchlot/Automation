"""发送邮件, 获取、删除邮件"""
import smtplib
import imapclient
import imaplib
imaplib._MAXLINE = 1000000

"""
msg = email.mime.multipart.MIMEMultipart()
msg['subject'] = 'Automation'
msg['From'] = 'guo123chong@163.com'
msg['to'] = 'guochong2016@gmail.com'
content = 'This email is from python3.6 automation'
msg.attach(email.mime.multipart.MIMEMultipart(content))
print(msg.as_string())
"""


def send_email():
    # 两个\n表示下面的内容为正文
    msg = 'From: {}\r\nTo: {}\r\nSubject: Automation\r\n\r\n' \
          'This ia an email from python3.6 automation'.format(my_email, destination_email)
    smtp_object = smtplib.SMTP_SSL('smtp.163.com', 465)
    print(type(smtp_object))
    print(smtp_object.ehlo())
    print(smtp_object.login(my_email, password))
    result = smtp_object.sendmail(my_email, destination_email, msg)
    print(result)
    smtp_object.quit()


def get_email():
    # 登录邮箱
    imap_163 = imapclient.IMAPClient('imap.163.com', ssl=True)
    login_status = imap_163.login(my_email, password)
    print('登录状态：', login_status)

    # 获取邮箱的文件夹列表并打印
    folders = imap_163.list_folders()
    print(type(folders))
    for folder in folders:
        print(folder)

    # 选择文件夹,根据IMAP搜索键，获取文件夹中邮件的uid
    imap_163.select_folder('INBOX', readonly=True)     # 可以忽略其返回值，如果文件夹不存在将抛出imap.error异常
    uids = imap_163.search(['ALL'])
    for uid in uids:
        print(uid)

    # 根据uid获取邮件内容
    raw_message = imap_163.fetch(uids[0], ['BODY[]'])
    print(raw_message)
    print(type(raw_message))
    imap_163.logout()


if __name__ == '__main__':
    my_email = input('Please input your email address: >>>')
    destination_email = input("Please input destination email: >>> ")
    password = input('Please input your password: >>>')
    send_email()
