# pip install flask
# create a folder 'templates' to store html files

from flask import Flask, render_template

app = Flask(__name__)

# templates ane folder lo index.html ani create chey
@app.route('/')
def home():
  return render_template('index.html')

app.run(debug = True)
