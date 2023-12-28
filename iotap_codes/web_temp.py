# IMPORTANT: connect temp sensor to GPIO 4
from flask import Flask
import w1thermsensor

sensor = w1thermsensor()
app = Flask(__name__)

@app.route('/')
def home():
    temp = sensor.get_temperature()
    return 'temp: {} degree C'.format(temp)
    # don't forget to reload the page to get new readings
if __name__ == '__main__':
    app.run(debug = True)
