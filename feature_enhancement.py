# -*- coding: utf-8 -*-
"""Feature_Enhancement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17xB7cB6eFZL4CWmbVABTgDw6LkN6UHLm
"""

#import packages
import pandas as pd
import numpy as np
import h5py

druginfo=pd.read_csv("*path/DATA/drugsinfo.csv")
KG_cell_line_feature=pd.read_excel('*path/DATA/KG_cell_line_feature.xlsx').rename(columns={'Unnamed: 0':'cell_line_name'})
KG_drug_feature=pd.read_excel('*/path/DATA/KG_drug_feature.xlsx').rename(columns={'Unnamed: 0':'drug_name'})
f1 = h5py.File('*path/DATA/A1_sign2.h5', 'r')# 2D_fingerprint similarty drug features
f2 = h5py.File('*path/DATA/A5_sign2.h5', 'r')# Physicochemistry similarity drug features

Inchkey=druginfo['InChIKey'].str.rstrip('\xa0')
cond=Inchkey.tolist()
Inchkey=druginfo['InChIKey'].str.rstrip('\xa0')
cond=Inchkey.tolist()
list(f1.keys())
keys = f1['keys'][:]
values = f1['V'][:]
keys = [key.decode() for key in keys]
# Create a dictionary of the data
data_dict1 = {key: values[i] for i, key in enumerate(keys)}
# Create a DataFrame from the dictionary
A1= pd.DataFrame(data_dict1)
myA1=A1.loc[:,cond]
list(f2.keys())
keys = f2['keys'][:]
values = f2['V'][:]
keys = [key.decode() for key in keys]
# Create a dictionary of the data
data_dict2 = {key: values[i] for i, key in enumerate(keys)}
# Create a DataFrame from the dictionary
A2= pd.DataFrame(data_dict2)
myA2=A2.loc[:,cond]
rename=dict(zip(druginfo['InChIKey'].str.rstrip('\xa0'), druginfo['drug_name']))
myA1=myA1.rename(columns=rename)
myA2=myA2.rename(columns=rename)
concat=pd.concat([myA1,myA2],axis=0)
drug_chemchecker_feature=concat.transpose().reset_index().rename(columns={'index':'drug_name'})

#concatenate KG_drug_feature with drug_chemchecker_feature
drug_feature=pd.merge(drug_chemchecker_feature,KG_drug_feature,on='drug_name')

#save drug_features in DATA directory

