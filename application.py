# flask for web app.
from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
# numpy for numerical work.
import numpy as np

import tensorflow.keras as kr

model = kr.models.load_model("model.h5")

# not using a separate file like in datarep project dao
# just testing here for now 
def predict_power(speed):
  if speed >24.4:
    return(0)
  if speed > 3 and speed < 24.4:
    #speed = np.array([speed])
    return (speed*2)
  elif speed > 10:
    return (speed*10)
  else:  
    #return model.predict(speed)
    return(speed*100)



# Create a new web app.
app = Flask(__name__, static_url_path='', static_folder='static')


# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')


  # Add model1 prediction route.
@app.route('/api/model1/<int:speed>')
def power(speed):
  #return predict_power(speed)
  
  return {"value": predict_power(speed)}

# Add model2 prediction route.
@app.route('/api/model2<int:speed>')
def uniform():
  return {"value": np.random.uniform()}

