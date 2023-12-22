import smtplib
#import RPi.GPIO as GPIO
import time

import subprocess

subprocess.run(["fswebcam", "image.jpg"])

#from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Camera Settings
#camera = PiCamera()
#camera.resolution = (2592, 1944)
#camera.framerate = 15

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'cuboidrandom@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'icceqmtjgktuijzt'  #change this to match your gmail password

#Set GPIO pins to use BCM pin numbers
#GPIO.setmode(GPIO.BCM)

#Set digital pin 17(BCM) to an input and enable the pullup
#GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Event to detect button press
#GPIO.add_event_detect(17, GPIO.FALLING)

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

sender = Emailer()

    #if GPIO.event_detected(17):
image = '/home/pranavsusarla/Desktop/IoTAP/image.jpg'
sendTo = 'ysrohitsai@gmail.com'
emailSubject = "Test Subject"
emailContent = "Test content"
sender.sendmail(sendTo, emailSubject, emailContent, image)
print("Email Sent")

 
