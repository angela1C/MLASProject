from flask import Flask, url_for, redirect, jsonify, render_template
# numpy for numerical work.
import numpy as np

# to import the models saved in the notebook
import joblib

model_poly3 = joblib.load('model_poly3.joblib')
mod_poly3 = joblib.load('model_poly3.pkl')


import tensorflow.keras as kr
from tensorflow.keras.models import load_model

model = kr.models.load_model("model.h5")
# two neural network models
NNmodel1 = load_model('model.h5')
NNmodel2 = load_model('model2.h5')

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

def predict_power_poly3(speed):
  return "polynomial"

# Create a new web app.
app = Flask(__name__, static_url_path='', static_folder='static')


# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')


  # Add model1 prediction route.
@app.route('/api/neuralnetwork1/<int:speed>')

def predict_power_NN_model1(speed):
  #speed = np.array(speed)

  if speed < 3.5:
    NN1pred = NNmodel1.predict([speed])
    min = 0
    NN1pred = NNmodel1.predict([speed])
    return {"value": NN1pred}
  elif speed > 24.4:
    return {"value": 0}
  else:
    NN1pred = NNmodel1.predict([speed])
    return {"value": str(NN1pred[0][0])} 


@app.route('/api/neuralnetwork2/<int:speed>')
def predict_power_NN_model2(speed):
  if speed < 3.5:
    return {"value": 0}
  elif speed > 24.4:
    return {"value": 0}
  else:
    NN2pred = NNmodel2.predict([speed])
    return {"value": str(NN2pred[0][0])} 


  
# Add polynomial3 prediction route.
# need to put upper and lower limits on this to stop negative values
@app.route('/api/polynomial3/<int:speed>')
def predict_power_poly3_model(speed):
  #return predict_power(speed)
  # I think I need to transform the wind speeds here.
  # maybe just do so manually or by squaring and cubing the inputs as it is only one at a time
  if speed >24.3:
    #poly3pred = model_poly3.predict([[speed, speed**2, speed**3]])
    return {"value": 0}
  
  if speed < 3.5:
    poly3pred = model_poly3.predict([[speed, speed**2, speed**3]])[0][0]
    NN1pred = NNmodel1.predict([speed])[0][0]


    return {"value": min(0,poly3pred) }
  #speed = np.array([[speed, speed**2, speed**3]])
  else:
    poly3pred = model_poly3.predict([[speed, speed**2, speed**3]])[0][0]
  #prediction = model_poly3.predict([[speed, speed**2, speed*3]])

    return {"value": str(poly3pred)}


@app.route('/api/polynomial4/<int:speed>')
def predict_power_poly4_model(speed):
  if speed >24.3:
    return(0)
  
  if speed <3:
    return (0)
  #speed = np.array([[speed, speed**2, speed**3]])
  else:
    # need to save and import poly4 model first
    poly4 = model_poly3.predict([[speed, speed**2, speed**3, speed**4]])

@app.route('/api/range/<int:speed>')
def predict_power_range(speed):
  # Turbine will always be powered off at speed values greater than 24.4
  if speed >24.3:
    return({"min":str(0), "max":str(0)})

  if speed ==0:
    return({"min":str(0), "max":str(0)})

  elif speed >0 and speed <24.3:
    # polynomial model is predicting negative values
    poly3pred = max(0,model_poly3.predict([[speed, speed**2, speed**3]])[0][0])
    #poly4 = model_poly4.predict([[speed, speed**2, speed**3, speed**4]])
    NN1pred = NNmodel1.predict([speed])[0][0]
    NN2pred = NNmodel2.predict([speed])[0][0]
 

    return {"min":str(min(poly3pred,NN1pred, NN2pred)),"max":str(max(poly3pred,NN1pred, NN2pred ))}
    
