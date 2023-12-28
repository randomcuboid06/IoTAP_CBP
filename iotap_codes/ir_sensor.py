import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setwarnings(False)
led = 26
ir = 4

gp.setup(led, gp.OUT)
gp.setup(ir, gp.IN)

while True:
  r = gp.input(ir)
  if r:
    gp.output(led, gp.HIGH)
  else:
    gp.output(led, gp.LOW)
  time.sleep(0.5)
  
  
