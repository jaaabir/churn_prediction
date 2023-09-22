import pandas as pd 
import numpy as np 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
import os
import pickle

def save_pkl(data, name):
    if 'pickles' not in os.listdir():
        os.makedirs('pickles')
        
    if not name.endswith('.pkl'):
        name = f'{name}.pkl'
        
    name = os.path.join('pickles', name)
    with open(name, 'wb') as file:
        pickle.dump(data, file)
    file.close()
    print(f'Saved the data to {name}')
    
    
def load_pkl(name):
    name = os.path.join('pickles', name)
    with open(name, 'rb') as file:
         data = pickle.load(file) 
    file.close()
    return data

class Age_Stage(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = age_feature(X)
        return X

def age_feature(x):
    stages = ['Teens', 'Adults', 'Middle Age Adults', 'Senior Adults']
    if x >= 12 and x <= 19:
        return 'Teens'
    elif x >= 20 and x <= 39:
        return 'Adults'
    elif x >= 40 and x <= 59:
        return 'Middle Age Adults'
    elif x >= 60:
        return 'Senior Adults'