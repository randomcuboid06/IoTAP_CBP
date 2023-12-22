import pywhatkit
import cv2

def send_image():
    me, rohit, chelli = '+919704728494', '+918465956672', '+919014669893'

    # img_path = r'C:\Users\admin\Desktop\VNR\IOT AP CBP\test.jpg'

    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    ret, frame = video.read()
    

    if ret:
        img_path = r'C:\Users\admin\Desktop\VNR\IOT AP CBP\test.jpg'
        cv2.imwrite(img_path, frame)
        pywhatkit.sendwhats_image(rohit, img_path, 'This image was automatically sent by a python script', 20, True, 5)

    video.release()

send_image()