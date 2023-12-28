import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)
gp.setwarnings(False)
led=26
gp.setup(led, gp.OUT)

user_input = input()
while True:
  if user_input == 1:
    gp.output(led, gp.HIGH)
  elif user_input == 0:
    gp.output(led, gp.LOW)
  else:
    print('Wrong input')
  user_input = input()
