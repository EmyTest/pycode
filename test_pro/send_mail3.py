import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib,mimetypes
import email.encoders
from email.mime.base import MIMEBase

msg = email.mime.multipart.MIMEMultipart()
'''
最后终于还是找到解决办法了：邮件主题为‘test’的时候就会出现错误，换成其他词就好了。。我也不知道这是什么奇葩的原因
'''

tolist=['2458125875@qq.com','2945950589@qq.com']
msg['Subject'] = 'xixi'
msg['From'] = 'mg5851@126.com'
tolist=['2458125875@qq.com','2945950589@qq.com']   #发送给多个人
# msg['To'] = '2458125875@qq.com'.join(tolist)
# msg['To'] = '2945950589@qq.com'.join(tolist)

content = '''
    你好，mango
            这是一封自动发送的邮件。

       hahhhhh
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

#smtp = smtplib

'''下面是添加附件的代码'''

filename = "D:\\testpro\\report\\log.txt"                     #附件名
fp = open(filename,'rb')
ctype,encoding = mimetypes.guess_type(filename)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream'
maintype,subtype = ctype.split('/',1)
m = MIMEBase(maintype,subtype)
m.set_payload(fp.read())
fp.close()

email.encoders.encode_base64(m)                                           #把附件编码

m.add_header('Content-disposition','attachment',filename=filename)    #修改邮件头
msg.attach(m)


smtp = smtplib.SMTP()
smtp.connect('smtp.126.com','25') #25是端口号
smtp.login('mg5851@126.com', '******')
smtp.sendmail('mg5851@126.com', tolist, msg.as_string())        #tolist  发送给多个人
smtp.quit()
print('邮件发送成功email has send out !')