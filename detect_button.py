from gpiozero import Button, Device
# from send_image import send_image
from gpiozero.pins.mock import MockFactory

Device.pin_factory = MockFactory()

button = Button(2)

while True:
    button.wait_for_press()
    print('Button was pressed')
    # send_image()



