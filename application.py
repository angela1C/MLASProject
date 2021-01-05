# flask for web app.
from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
# numpy for numerical work.
import numpy as np

import tensorflow.keras as kr

model = kr.models.load_model("model.h5")

# not using a separate file like in datarep project dao

def predict_power(speed):
  if speed >24.4:
    return(0)
  if speed < 24.4:
    speed = np.array([speed])
    return model.predict(speed)



# Create a new web app.
app = Flask(__name__, static_url_path='', static_folder='static')


# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')



# Add uniform route.
@app.route('/prediction')
def predict_power():
  #return {"value": np.random.uniform()}
  return model.predict

# Add normal route.
@app.route('/testing')
def testing():
  return "hello"

  # Add normal route.
@app.route('/api/power<speed>')
def power():
  return "hello"