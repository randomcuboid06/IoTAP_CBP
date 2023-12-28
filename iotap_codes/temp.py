# IMPORTANT: connect temp sensor to GPIO 4
import w1thermsensor

sensor = w1thermsensor()

while True:
  temp = sensor.get_temperature()
  print(temp)
