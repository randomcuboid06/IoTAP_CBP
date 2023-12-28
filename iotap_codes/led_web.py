# NOT WORKING SHOULD SEE
from flask import Flask, render_template, request, redirect
import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(26, gp.OUT)


app = Flask(__name__)

# templates ane folder lo index.html ani create chey
@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    state = request.form['state']
    if state == 'on':
      gp.output(26, gp.HIGH)
    elif state == 'off':
      gp.output(26, gp.LOW)
    else:
      print('Wrong input!')
    
  else:
    return render_template('index.html')

app.run(debug = True)
