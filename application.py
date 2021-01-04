# flask for web app.
from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = Flask(__name__, static_url_path='', static_folder='static')

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}