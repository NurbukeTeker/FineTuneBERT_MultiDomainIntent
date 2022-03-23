# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:54:14 2022

@author: nurbuketeker
"""
from datasets import load_dataset
import pandas as pd
from plotDataset import plotData

def getCLINCData():
    dataset_small_train = load_dataset("clinc_oos", "small",split="train")
    dataset_small_test = load_dataset("clinc_oos", "small",split="test")
    
    df_train = pd.DataFrame(dataset_small_train)
    df_test = pd.DataFrame(dataset_small_test)
    
    value_counts = df_train['intent'].value_counts()
    value_counts = value_counts.to_dict()
    
    selectedIntents = [key for key in value_counts.keys() if value_counts[key] >= 50]
      
    df_train = df_train[df_train.intent.isin(selectedIntents)]
    df_test = df_test[df_test.intent.isin(selectedIntents)]
    
    value_counts = df_train['intent'].value_counts()
    value_counts = value_counts.to_dict()
    len(value_counts)
       
    plotData(value_counts,"figures/clincData")
    
    return df_train, df_test