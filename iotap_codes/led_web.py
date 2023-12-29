from flask import Flask, render_template, request
import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setwarnings(False)
led=26
gp.setup(led, gp.OUT)

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        state = request.form['led']
        if state == 'on':
            gp.output(led, gp.HIGH)
        elif state == 'off':
            gp.output(led, gp.LOW)
        else:
            print('Enter correct state!!')
        return render_template('index.html')
    else:
        return render_template('index.html')
  
if __name__ == '__main__':
    app.run(debug=True)
