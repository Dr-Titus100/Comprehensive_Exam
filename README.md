# Dark Matter Halo Density Profile Calibration

* Author: Titus Nyarko Nde (Computing Ph.D. - Data Science emphasis)
* Course: Comprehensive Exam
* Semester: Fall 2022

## Overview
In this tutorial, we calibrate dark matter density profiles using machine learning methods. Density calibration from gravitational lensing is one of the most important problems in cluster cosmology. The main objectives of this tutorial include: 
* Use neural network ensembles to better capture the complexity of density profiles and achieve more accurate density calibration. 
* Quantify prediction uncertainties (hereafter error bars). The idea is to make interval predictions rather than a single-point prediction in the case of the analytic models. This will help us capture the effect of differences in cosmology in our predictions.

A synthesis paper based on dark matter halo density profile calibration is included in the directory `Synthesis_Paper`. This is a comprehensive review of four main seed papers, namely:


 * Paper I: Dependence of the outer profiles of halos on their mass accretion rate [Diemer & Kravtsov, 2014](https://iopscience.iop.org/article/10.1088/0004-637X/789/1/1).
This paper studies the density profile of dark matter halos at large radii using data from N-body simulations. They also proposed a new analytic model for calibrating halo density profiles.

 * Paper II: The mass and galaxy distribution around SZ-selected clusters [Shin et al., 2021](https://academic.oup.com/mnras/article-abstract/507/4/5758/6366263?redirectedFrom=fulltext&login=true).
This paper measures halo density profiles from weak-lensing and galaxy number density profiles. They also considered the density profiles at large radii. They used observational data from the Atacama Cosmology Telescope and the Dark Energy Survey.

 * Paper III: A dynamics-based density profile for dark halos – I. Algorithm and basic results [Diemer, 2022](https://academic.oup.com/mnras/article-abstract/513/1/573/6561624?redirectedFrom=fulltext&login=true).
This paper presents a novel algorithm to dynamically disentangle the inner and outer regions of halos and model them separately. The data used is generated from N-body simulations.

 * Paper IV: The impact of baryons on massive galaxy clusters: halo structure and cluster mass estimates [Henson et al., 2017](https://academic.oup.com/mnras/article/465/3/3361/2454758?login=true).
This paper measures the impact of baryons (ordinary matter) on the density profiles of massive galaxy clusters. They used data from the BAHAMAS (BAryons HAlos MAssive System) and MACSIS (MAssive ClusterS and Intercluster Structure) hydrodynamic simulations.



## How to Use Code
Note: I assume the user of this repo is already a Python user and at least has either Anaconda or Miniconda or Miniforge installed. The person should have access to at least Jupyter Notebook or Jupyterlab. You can equally run the code using Visual studio code or Pycharm or Google colab. All Jupyter notebooks regarding this computing artifact are in the folder `Computing_Artifact`.

To use the code in this repo follow the following steps.
* Clone the repo using the following command.

```
git clone https://github.com/Dr-Titus100/Comprehensive_Exam.git
```
You may also fork the repo if interested.


* Install packages. All the packages used in the notebook and their versions are listed in the `requirements.txt` file. Activate your python environment and run the following command in the terminal to install all the packages at once.

```
pip install -r requirements.txt
```

Note: You may create a new Python environment to run this project. This ensures your existing projects are uninterrupted. To create a new Python environment use the following command:

```
conda create --name <env_name> python=<version>
```


## Submitting Jobs
For the DK14 profile, it takes a long time to compute the mean squared error for the entire test set. I computed the MSE for the entire test by submitting a job on the R2 cluster. The files in the directory `Multiprocessing`. It is advisable to run the `.py` file by submitting a job on a cluster. I have also uploaded a sample bash script in that directory, which I used to submit my job on the R2 cluster. To submit a job simply run the following command on a cluster node (make sure you are not on the login node).

```
sbatch Multiprocessing.sh
```

I have provided further comments in the `.sh` file. Those comments will be useful for anyone who wants to run the Python script. 

* If a module is missing, then you have to add a line in the `.sh` file to load the module.
```
module load <Path/to/module>
```


## Using Saved Models
The models might take time to run on a local computer. Hence, we saved all the models so that a user does not necessarily have to run the entire notebook to train the models before interacting with them. This means you can use the models without training them yourself from scratch. The models were saved in two formats:

* `.h5` format: This method saves the entire model in a single file. It consumes less space
* `Protocol Buffer` format: This is the default saving format in Tensorflow. It is fast to save and load but saves the model into a folder in multiple files. This approach consumes much more space than the `.h5` format.



* To load the models, use the following command.
```
from tensorflow.keras.models import load_model
model = load_model('model.h5')  # the .h5 format
```
or 
```
model = load_model('model') # the protocol buffer format, where `model` is the name of the folder containing the multiple files.
```


* Once a model is loaded successfully, we can use the loaded model by using the following command.
```
model.<Attribute>
```

For instance, we use the following
```
model.predict(test_data)
```
to make predictions on the test. Specifically, if you want to know how to make multiple predictions with the Monte Carlo dropout ], see the `UncertaintyQuantification` notebook. For the Deep Ensembles, all the individual models are saved so we can load all of them and use each of them to predict. Alternatively, see the `UncertaintyQuantification` notebook.


Note: You can also retrain your own data using an already trained model once your data satisfy the same conditions as those used to train the models in the first place. In this case, you do not have to necessarily recompile the model again. This method leads to faster training time and sometimes leads to better performance. To retrain the loaded model, simply use the following command.

```
model.fit(X_train, y_train)
```



See the following links for more details on saving, loading, and retraining saved models:
* [Save and load Keras models](https://www.tensorflow.org/guide/keras/save_and_serialize)
* [Is it possible to retrain a previously saved keras model?](https://stackoverflow.com/questions/51854463/is-it-possible-to-retrain-a-previously-saved-keras-model)
* [How to Save and Load Your Keras Deep Learning Model](https://machinelearningmastery.com/save-load-keras-deep-learning-models/)

