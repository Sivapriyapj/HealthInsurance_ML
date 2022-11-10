# Health Insurance Predictor
## Problem description
Health insurance provisions need to be allocated according to the physical and mental health status of a patient and the degree of disability he/she faces. This project predicts analyses the same for candidates with a variety of mental and physical health challenges and predicts if he/she is being given the required insurance that they require.

## About the project


After analyzing different algorithms, fine tuning them and validating them, final model was selected to be XG Boost and has been trained since XG Boost gave the best validation accuracy and AUC for the predictions.    

The predictions can be made by running test.py file.    

The model has been deployed using flask during production and waitress fro deployment.    

The same has been containarized using docker.


## How to run the prediction service on your system
* Item1
* Item 2




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

