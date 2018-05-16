from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("mg5851@126.com","******")
    smtp.sendmail("mg5851@126.com","2458125875@qq.com",msg.as_string())
    smtp.quit()
    print('email has send out!')

    '''查找测试报告目录，找到最新生成的测试报告文件'''
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport+"\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new
if __name__=='__main__':
    test_dir = 'F:\\pycode\\test_progect\\test_case'
    test_report = 'D:\\testpro\\report'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    now = time.strftime("%Y-5m-%d %H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况: ')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)

