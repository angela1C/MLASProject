# MLASProject

This repository contains my submission for the Machine Learning and Statistics Project as part of the requirement for the for the Machine Learning and Statistics module at GMIT as part of the Higher Diploma in Computing and Data Analytics programme.

## Project Instructions
The full project instructions are contained in the `Project_Instructions` pdf file.

A web service must be created that uses machine learning to make predictions based on the data set `powerproduction` available on Moodle. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. The web service will respond with predicted power values based on speed values sent as HTTP requests. 

## Repository Contents
- A Jupyter notebook `wind_project.ipynb` that trains a model using the data set, explains the model and gives an analysis of its accuracy.

- A Python script `application.py` that runs a web service based on the models developed in the notebook.

- A Dockerfile to tell docker how to build and run the web service application in a container.
- This README file.
- A requirements.txt file containing the python packages required to run the web service.
- A `models` folder containing the machine learning models developed in the notebook. 
    * The neural network models are saved with the `.h5` extension. 
    * The polynomial regression models are saved with the `.pkl` and `.joblib` extensions. 
- A `static` folder containing the `index.html` page for the web service application.
- A .dockerignore file that tells docker to ignore certain files in certain circumstances.
- A .gitignore file
- The dataset has been saved as `df.csv` but it also available [here](https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv) at [github.com/ianmcloughlin](https://github.com/ianmcloughlin)

### How to download the repository


Go to the URL for the repository at https://github.com/angela1C/Mlasproject and click the green Code button. Follow instructions to clone to your local machine.


### How to run the code

Python 3 was used to develop this project and is needed to run the code in the notebook. Python 3 can be downloaded from the official Python website at https://www.python.org/downloads/. It can also be downloaded using the Anaconda Python distribution at https://www.anaconda.com/distribution/.

The Jupyter Notebook `wind_project.ipynb`  can be viewed directly in this GitHub repository in a browser without Python 3 being installed. On occasion the Jupyter Notebook may not render correctly in which case the URL https://github.com/angela1C/MLASProject/blob/main/wind_project.ipynb can be copied and pasted in to the Jupyter nbviewer at https://nbviewer.jupyter.org. This will render a static version of the notebook in the browser.
If the repository is downloaded it can be run locally by navigating to the folder and entering the command `jupyter lab` or `jupyter notebook` on the command line. This will open Jupyter in the browser. The `wind_project.ipynb` notebook can be opened then within the Jupyter session. Once opened you can can select Restart and Run All from the Kernel menu.

The following Python packages were used for this project:

- Python3 available at https://www.python.org
- Jupyter Notebook at https://jupyter.readthedocs.io
- Python Pandas Library. A fast, powerful, flexible and easy to use open source data analysis and manipulation tool at https://pandas.pydata.org
- Scikit-learn for Machine Learning in Python at https://scikit-learn.org
- SciPy. A Python-based ecosystem of open-source software for mathematics, science, and engineering at https://docs.scipy.org

- NumPy. The fundamental package for scientific computing with Python at https://numpy.org

- Matplotlib. A comprehensive library for creating static, animated, and interactive visualizations in Python at https://matplotlib.org
- Seaborn. A Python data visualization library based on matplotlib at https://seaborn.pydata.org/
- Keras Tensorflow. An open source library for training and developing machine learning models at https://www.tensorflow.org/guide/keras/sequential_model

These packages can be installed if necessary on the command line using `pip install <package-name>`. Most of them come with the Anaconda distribution of Python 3. 
    
---    
    
### Web Service Application 

The `Docker` file included in this repository contains the instructions to build a docker image.
    
The following instructions can be used to get the web server up and running:

- Clone the repository to your local machine

- Check if docker is installed on your machine using `docker --version`.  
If not you will need to install docker. Note that this may take some time. Go to https://www.docker.com

- `docker build -t windpower-app . `
This will build a docker image in your repository in the current folder (`.`)
The `-t` flag assigns a tag name to the application, otherwise the container id is used.

- `docker run -d -p 5000:5000 windpower-app`
Once this is running you can access the app on your browser at the local host.

- `docker image ls` will list the images in the container

- `docker container ls` will list the container ids (if you need to kill the container)
- `docker kill <container-id>` to kill the container
- `docker rm <container-id>` to remove a container.

Note that Tensorflow may cause some problems when using docker. If you do not have docker installed you can alternatively run the Flask application program on your local machine using the local host, First create a virtual environment and install the packages required into the virtual environment using the `requirements.txt` file. Then navigate to the local host on the browser to run the application where you will interact with the html page.
The webpage `index.html` is saved in the `static` folder.

### To run Flask application on Linux / Mac
- `python -m venv venv` to create a virtual environment.
- `source venv/bin/activate` to activate the virtual environment
- `pip install -r requirements.txt` to install the required packages into the virtual environment.
- `export FLASK_APP=application` to set the name of the server program as an environmental variable
- `export FLASK_ENV=development` optionally to set the development environment for debugging mode.
- `flask run` to run the server program `application.py`
- This will start the application on http://127.0.0.1:5000/. Copy the link into your browser to access the web service program.
- `deactivate` to leave the virtual environment and go back to using the system wide environment.

###  To run Flask application on Windows
Replace:
- `source venv/bin/activate` with `.\venv\Scripts\activate.bat`
- `export FLASK_APP=application` with `set FLASK_APP=application`


### Using the Web service application:

- Enter a wind speed value between 0 and 25 representing wind speeds in metres per second.
- Click the button.
- The page will respond by outputting the predictions for wind turbine power output based on the machine learning models trained on the dataset.

- The predictions give a range for the minimum and maximum power values that can be expected for the wind speed value entered.
- Note that for wind speeds above 24.4 metres per second, the turbines are switched for safety reasons.
### References

All references used for developing the machine learning models are documented at the end of the `wind_project.ipynb` jupyter notebook. All quotations are numbered. Other resources were used in researching the project which are also listed in the reference section.

- [Docker](https://www.docker.com/resources/what-container)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [PYPI](https://pypi.org/) for finding and installing Python packages  

