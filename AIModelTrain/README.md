# AIModelTrain

## Table of Contents

   * [Overview](#overview)
   * [Folder Structure](#folder-structure)
   * [File Contents](#file-contents)
   * [Deployment](#deployment)
        * [How to Install and Build the Packages](#how-to-install-and-build-the-packages)
   * [More things to add](#more-things-to-add)
   * [Authors](#authors)
   * [Acknowledgments](#acknowledgments)



## Overview

This Module/Service/Project aims to provide classes with methods that use data to train a machine learning
model for the AI project being developed.

The classes have been structured in a way that they can be used across various projects in order to allow the
reusability or code.

The classes have been implemented using **Python 3.6** and the code supports distributed computation
using **Apache Spark 2.4.0**.


## Folder Structure

- **aimodeltrain**
    - **bl**: (Business Logic) Contains all the classes and methods being used to train the ML model 
    - **dao**: (Data Access Object) Any class used for I/O purposes are defined in this folder
    - **driver**: Entry point to use the service
    - **exceptions**: Contains the various exceptions that will be used throughout the classes being implemented 
    for the 
    - **utils**: Common utilities being used throughout the module
- **resources**: Will store all the configuration files 


## File Contents

    
    
- **driver**

    - *AbstractTrainDriver.py*: This file contains an abstract class with the abstract function(s) that all Train Drivers need to implement.
    - *AbstractTrainDriverFactory.py*: Selects which Train Driver to return (Model Train Driver or Anomaly Detection Train Driver).
    - *ModelTrainDriver.py*: This file contains a model train driver, with a class function to run the flow for training a model on provided data.
    - *AnomalyDetectionTrainDriver.py*: This file contains an anomaly detection train driver, with a class function to run the flow for caclulating anomaly scores for the provided data.


    
## Deployment

Each of these Modules are documented for the purpose of re-usability across projects. 

#### Prerequisites:

-  AICommonsPython package should be installed

#### Steps to create a pip Package:

- Take the parent directory of the python package
- The folder should contain: 
   - relevant python package i.e. aimodeltrain
   - a resources folder, if any 
   - setup.py
- Contents of setup.py:

````
from setuptools import setup

setup(
    name='aimodeltrain',
    version='0.1',
    description='i2c model training module',
    url='',
    author='afarooq01',
    author_email='afarooq01@i2cinc.com',
    liscence='i2c',
    packages=['aimodeltrain'],
    zip_safe=False)

````

- In the package's __init__.py import the classes that you want to expose

Import:


    from .driver.ModelTrainDriver import ModelTrainDriver



#### How to Install and Build the Packages


Change your directory to the folder containing setup.py and run the following command:
	
    pip3 install -e .
    
#### Inputs and outputs 

- What inputs need to be given to the module

    `train_data, feature_list, model_name, model_code`


- What outputs will this module give

    `trained_model`

## More things to add

## Authors

* **Aleena Farooq** - *afarooq01@i2cinc.com*
* **Samreen Fatima** - *sfatima@i2cinc.com*
* **Sana Mahmood** - *smahmood@i2cinc.com*
* **Uzair Ahmad** - *uahmad@i2cinc.com*
* **Maha Yaqub** - *myaqub@i2cinc.com* 
* **Hamza Rafiq** - *hrafiq@i2cinc.com* 


## Acknowledgments

* **Alishan Rao** - *arao@i2cinc.com*

