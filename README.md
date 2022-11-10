# Health Insurance Predictor
## Problem description
Health insurance provisions need to be allocated according to the physical and mental health status of a patient and the degree of disability he/she faces. This project analyses the same for candidates with a variety of mental and physical health challenges and predicts if he/she is being provided health insurance that they require.

## About the project


After analyzing different algorithms, fine tuning them and validating them, final model was selected to be XG Boost and has been trained since XG Boost gave the best validation accuracy and AUC for the predictions.    

The predictions can be made by running test.py file.    

The model has been deployed using flask during production and waitress fro deployment.    

The same has been containarized using docker.

## Installing dependencies and activating the environment

* Install pipenv : **pip install pipenv**
* Install python version 3.8 or greater
* Install other required libraries: **pipenv install numpy pandas sklearn====1.1.3 flask waitress====2.1.2**
* activating the shell : **pipenv shell**
* Install xgboost : **pipenv install xgboost**
* Install any dependency you need to as shown in the error message, if it throws an error as some module is missing while running the program
* fork or clone the repository to working directory if needed to run from IDE.


## How to run the prediction service on your system


* build the image using  **docker build -t zoomcamp-test .** on the terminal of your IDE.
* Open a new terminal and run **docker run -it -p 9696:9696 zoomcamp-test:latest**
* open a new terminal in your IDE and type : **python predict_test.py**

Alternatively, you can directly run it from the terminal :

* Download all the files/clone the repo to your system
* Navigate to the project directory in terminal
* run **python predict.py**
* run **python predict_test.py**


|File name|Description|
|---------|-------------------------------------------------------|
|Dockerfile | file to build and run the docker image in your system|
|patient-characteristics-survey-pcs-2013-1.csv|data set used to train the models |
|notebook.ipynb|For all the preprocessing, EDA, model                                        training,validation,correlation,feature importance analysis and tuning.
|predict.py|script to run the flask app|
|Train.py|script to train and save the final model|
|predict_test.py| file to print output response of the model.|
|Pipfile & Pipfile.lock|pipenv files to prepare virtual enviroment| 
|model_Final.bin| The file in which trained model/ weights are pickled and saved|

