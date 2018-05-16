import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
'''
最后终于还是找到解决办法了：邮件主题为‘test’的时候就会出现错误，换成其他词就好了。。我也不知道这是什么奇葩的原因
'''
msg['Subject'] = 'xixi'
msg['From'] = 'mg5851@126.com'
msg['To'] = '2458125875@qq.com'
content = '''
    你好，mango
            这是一封自动发送的邮件。

       hahhhhh
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

#smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com','25') #25是端口号
smtp.login('mg5851@126.com', '*****')
smtp.sendmail('mg5851@126.com', '2458125875@qq.com', msg.as_string())
smtp.quit()
print('邮件发送成功email has send out !')