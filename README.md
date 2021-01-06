# MLASProject
Repository for Machine Learning and Statistics Project

This repository contains my submission for the Machine Learning and Statistics Project as part of the requirement for the for the Machine Learning and Statistics module at GMIT as part of the Higher Diploma in Computing and Data Analytics programme.

This repository contains the Jupyter notebook x.ipynb which contains the main body of the work. 

In this project you must create a web service that uses machine learning to make pre- dictions based on the data set powerproduction available on Moodle. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. You must then develop a web service that will respond with predicted power values based on speed values sent as HTTP requests. Your submission must be in the form of a git repository containing, at a minimum, the following items.
Jupyter notebook that trains a model using the data set. In the notebook you should explain your model and give an analysis of its accuracy.
- Python script that runs a web service based on the model, as above.
- Dockerfile to build and run the web service in a container.
- Standard items in a git repository such as a README. 
- To enhance your submission, you might consider developing and comparing more than one model. 
- Rest assured, all the above concepts will be explored in lecture videos and other materials in the coming semester.


### How to download the repository


Go to the URL for the repository at https://github.com/angela1C/Mlasproject and click the green Code button. Follow instructions to clone to your local machine.

### Files Contained 

- requirements.txt file: This text file lists the packages required to run the project
- .dockerignore file
- .gitignore file
- Dockerfile



### How to run the code

Python 3 was used to develop this project and is needed to run the code in the notebook. Python 3 can be downloaded from the official Python website at https://www.python.org/downloads/. It can also be downloaded using the Anaconda Python distribution at https://www.anaconda.com/distribution/.

The Jupyter Notebook tasks.ipynb itself can be viewed directly in this GitHub repository in a browser without Python 3 being installed. On occasion the Jupyter Notebook may not render correctly in which case the URL https://github.com/angela1C/MachineLearningTasks2020 can be copied and pasted in to the Jupyter nbviewer at https://nbviewer.jupyter.org where you enter the location of a Jupyter Notebook and click Go to have it rendered there as a static version of the notebook.

The following Python packages were used for this project:

- Python3 available at https://www.python.org
- Jupyter Notebook at https://jupyter.readthedocs.io
- Python Pandas Library. A fast, powerful, flexible and easy to use open source data analysis and manipulation tool at https://pandas.pydata.org
- Scikit-learn for Machine Learning in Python at https://scikit-learn.org
- SciPy. A Python-based ecosystem of open-source software for mathematics, science, and engineering at https://docs.scipy.org

- NumPy. The fundamental package for scientific computing with Python at https://numpy.org

- Matplotlib. A comprehensive library for creating static, animated, and interactive visualizations in Python at https://matplotlib.org
- Seaborn
- Keras Tensorflow ..

These packages can be installed if necessary on the command line using pip install <package name>. Most of them come with the Anaconda distribution of Python 3. 

The notebook containing all the work is named X.ipynb. If the repository is downloaded it can be run locally by navigating to the folder and entering the command jupyter lab or jupyter notebook on the command line. This will open Jupyter in the browser. The tasks notebook can be opened then within the Jupyter session. Once opened you can can select Restart and Run All from the Kernel menu.


---

The following instructions can be used to get the web server up and running:

- Clone the repository to your local machine

- Check if docker is installed on your machine using `docker --version`
If not you will need to install docker.

- `docker build -t windspeed-app . `
This will build a docker image in your repository, in the current folder (`.`). An image is a collection of files, a design for the container.
The `-t` flag assigns a tag name to the application, otherwise the container id is used.

- `docker run -d -p 5000:5000 windspeed-app`
Once this is running you can access the app on your browser at the local host.

- `docker image ls` will list the images. 

- `docker container ls` will list the container ids (if you need to kill the container.)


Tensorflow may cause some problems when using docker. For this reason you can alternatively create a virtual environment and install the packages required into the virtual environment. Then navigate to the local host on the browser to run the app.




- python -m venv venv 
- source venv/bin/activate
- pip install -r requirements.txt
- export FLASK_APP=application
- export FLASK_ENV=development
- flask run


---
FROM python:3 

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=application.py

CMD flask run --host=0.0.0.0

---

https://www.tensorflow.org/install/pip

Tensorflow doesn't seem to work in the venv with flask when I try to install the requirements.txt
I've followed the instructions here to install tensorflow with pip.
I've been using it fine all along in jupyter notebook to train the model.
However installing into a virtual environment is problematic so maybe I should not be using a virtual environment.
I've upgraded pip using ` pip install --upgrade pip`
- `pip install --upgrade tensorflow`
I've successfully installed tensorflow
>Successfully installed flatbuffers-1.12 grpcio-1.32.0 numpy-1.19.4 tensorflow-2.4.0 tensorflow-estimator-2.4.0 typing-extensions-3.7.4.3

And verified the install using
`python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"` which seemed fine.

If I can't get docker working properly with tensorflow then I'll have to just use flask in a virtual environment.
I'll try again tomorrow loading the requirements.txt file


---

Now when I run the flask app I get the message below about tensorflow but it seems to be ok.


2021-01-05 18:52:10.358879: I tensorflow/compiler/jit/xla_cpu_device.cc:41] Not creating XLA devices, tf_xla_enable_xla_devices not set
2021-01-05 18:52:10.358874: I tensorflow/compiler/jit/xla_cpu_device.cc:41] Not creating XLA devices, tf_xla_enable_xla_devices not set
2021-01-05 18:52:10.359778: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2021-01-05 18:52:10.359778: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

---

Had to pip install joblib  library and added to requirements.txt
