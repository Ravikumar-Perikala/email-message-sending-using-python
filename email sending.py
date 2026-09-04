import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg['subject']='inviting for my brothe marriage'
msg['From']='ravikumar19191947@gmail.com'
msg['To']='manohar37manu@gmail.com'
msg.set_content('''Dear manohar bava,
greeting from bavamaridi.....
welcome to my brother marriage function if you not come my brother marriage i will stop . bava you and my sister come our home in one month before.nanu my own car to send from pickup you and my sister.
best regardes,
perikala Ravikumar(IAS) ''')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("ravikumar19191947@gmail.com", "zfscqjjyxfujosjt")
server.send_message(msg)
print('Email Sent Sucessfully')
server.quit()