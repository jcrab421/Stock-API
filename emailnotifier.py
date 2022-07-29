import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr=''
to_addr=['']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='Stock price alert for Apple Inc.'

body='Stock price alert: Hold Stock. Price is between 130 and 200'

msg.attach(MIMEText(body,'plain'))

email='' #put email here
password='' #put password here

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()





