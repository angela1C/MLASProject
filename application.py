from flask import Flask, url_for, redirect, jsonify, render_template
# numpy for numerical work.
import numpy as np

# to import the models saved in the notebook, I saved the polynomials in both pickle and joblib
import joblib
model_poly3 = joblib.load('models/model_poly3.joblib')
mod_poly3 = joblib.load('models/model_poly3.pkl')
model_poly4 = joblib.load('models/model_poly4.joblib')
mod_poly43 = joblib.load('models/model_poly4.pkl')


import tensorflow.keras as kr
from tensorflow.keras.models import load_model

#model = kr.models.load_model("model.h5")
# load the two neural network models
NNmodel1 = load_model('models/model.h5')
NNmodel2 = load_model('models/model2.h5')

# Create a new web app.
app = Flask(__name__, static_url_path='', static_folder='static')

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')
  #return render_template('index.html')

# Add neural network1 prediction route.
@app.route('/api/nn1/<int:speed>')
@app.route('/api/nn1/<float:speed>')
def predict_power_NN_model1(speed):
  #speed = np.array(speed)

  if speed > 24.4:
    return {"value": 0}
  else:
    NN1pred = NNmodel1.predict([speed])[0][0]
    return {"value": str(NN1pred)} 

# Add neural network2 prediction route.
@app.route('/api/nn2/<int:speed>')
@app.route('/api/nn2/<float:speed>')
def predict_power_NN_model2(speed):
  if speed >24.4:
    return {"value": 0}

  else:
    NN2pred = NNmodel2.predict([speed])[0][0]
    return {"value": str(NN2pred)} 


# Add polynomial3 prediction route.
# need to put upper and lower limits on this to stop negative values
@app.route('/api/poly3/<int:speed>')
@app.route('/api/poly3/<float:speed>')
def predict_power_poly3_model(speed):

  # manually transforming the inputs for now
  if speed >24.4:
    #poly3pred = model_poly3.predict([[speed, speed**2, speed**3]])
    return {"value": 0}
  
  else:
    poly3pred = model_poly3.predict([[speed, speed**2, speed**3]])[0][0]

    return {"value": str(poly3pred)}


# add route for the 4th order polynomial
@app.route('/api/poly4/<int:speed>')
@app.route('/api/poly4/<float:speed>')
def predict_power_poly4_model(speed):
  if speed >24.4:
    return {"value": str(0)}
  
  else:
    # need to save and import poly4 model first
    poly4pred = model_poly4.predict([[speed, speed**2, speed**3, speed**4]])[0][0]
    return {"value":str(poly4pred)}

# Here I will add a route to predict a range of values for each wind speed value entered
# a minimum value and a maximum value
@app.route('/api/range/<int:speed>')
@app.route('/api/range/<float:speed>')
def predict_power_range(speed):
  # Turbine will always be powered off at speed values greater than 24.4
  if speed >24.4:
    return({"min":str(0), "max":str(0)})

  # cannot predict a power value for a non wind-speed so predict zero power for zero wind
  # can also limit the range of numbers the user can enter I guess
  if speed ==0:
    return({"min":str(0), "max":str(0)})

  elif speed >0 and speed <24.5:
    # polynomial model is predicting negative values
    poly3pred = max(0,model_poly3.predict([[speed, speed**2, speed**3]])[0][0])

    poly4pred= max(0,model_poly4.predict([[speed, speed**2, speed**3, speed**4]])[0][0])
    
    NN1pred = NNmodel1.predict([speed])[0][0]
    NN2pred = NNmodel2.predict([speed])[0][0]
 

    return {"min":str(round(min(poly3pred,poly4pred,NN1pred, NN2pred),6)),"max":str(round(max(poly3pred,poly4pred,NN1pred, NN2pred ),6))}
    
