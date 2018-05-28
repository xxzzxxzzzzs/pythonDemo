# kuwkgizistzsbfgg
import  smtplib
from  email.mime.text import MIMEText
# smtp服务器
SMTPServer="smtp.qq.com"
# pop3服务器
sender="740866631@qq.com"
#发邮件的邮箱密码
passwprd="kuwkgizistzsbfgg"

message="先你要登陆qq的webmail，在“设置”，“账户”中打开pop3和smtp，然后在客户端的outlook或foxmail创建新的账户，选择pop/imap/smtp的账户类型，在服务器地址中填写接收服务器为pop.qq.com，发送服务器smtp.qq.com，然后填写账户密码即可完成设置。"
# 内容
msg=MIMEText(message)
# 标题、
msg["Subject"]="lalala"
# 发送者
msg["From"]=sender
# 创建smtp服务器
mailSever=smtplib.SMTP_SSL(SMTPServer,465)
# 登录邮箱
mailSever.login(sender,passwprd)
# 发送邮件
mailSever.sendmail(sender,["xxzzxxzzzzs@163.com"],msg.as_string())
mailSever.quit()