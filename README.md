# Kidney_disease_classification

# WorkFlows

1. update config.yaml
2. update secrets.yaml
3. update `parmas.yaml`
4. update the entity
5. update the configuration manager in src config.
6. update the components
7. Update the pipeline.
8. Update the main.py
9. Update the dav.yaml.
10. app.py





# How to run ?

## STEPS?

'''
cone the repository
https://github.com/Abhikkumar619/Kidney_disease_classification

## SETPS 1- Create a conda environement after opening the repository.
conda create -p environment_name python==version.

## STEPS 2 - Install requirement.txt
pip install -r requirement.txt



### dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/Abhikkumar619/Kidney_disease_classification.mlflow \
MLFLOW_TRACKING_USERNAME=Abhikkumar619 \
MLFLOW_TRACKING_PASSWORD=b515b18fe70cac23bd1c8591a7c54e188845b00c \
python script.py

Run this to exort as env variabels: 

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Abhikkumar619/Kidney_disease_classification.mlflow 

export MLFLOW_TRACKING_USERNAME=Abhikkumar619

export MLFLOW_TRACKING_PASSWORD=b515b18fe70cac23bd1c8591a7c54e188845b00c

