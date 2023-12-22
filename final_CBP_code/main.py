from signal import pause
from gpiozero import Button

import smtplib
import time
import subprocess

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Emailer:
    def sendmail(self, recipient, subject, content, image):

        #Create Headers
        emailData = MIMEMultipart()
        emailData['Subject'] = subject
        emailData['To'] = recipient
        emailData['From'] = GMAIL_USERNAME

        #Attach our text data
        emailData.attach(MIMEText(content))

        #Create our Image Data from the defined image
        imageData = MIMEImage(open(image, 'rb').read(), 'jpg')
        imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
        emailData.attach(imageData)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
        session.quit


#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'cuboidrandom@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'icceqmtjgktuijzt'  #change this to match your gmail password


sender = Emailer()


def prog():
    subprocess.run(['fswebcam', '-r', '640x480', '-S', '40', 'image.jpg'])
    image = '/home/user/Desktop/IoTAP_CBP_08_57_63/image.jpg'
    sendTo = 'pranavsusarla2@gmail.com'
    emailSubject = "Test Subject"
    emailContent = "Test content"
    sender.sendmail(sendTo, emailSubject, emailContent, image)
    print("Email Sent")
    
button = Button(18, pull_up=False)

try:
    button.when_pressed = prog
    pause()
finally:
    pass

 