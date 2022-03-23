# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:18:55 2022

@author: nurbuketeker
"""
import pandas as pd 
from  plotDataset import plotData

def getACIDData():
    df_acid_train = pd.read_csv("ACIDData/customer_training.csv")
    
    acid_train_texts = df_acid_train["UTTERANCES"].tolist()
    acid_train_labels = df_acid_train["INTENT_NAME"].tolist()
    
    df_acid_test = pd.read_csv("ACIDData/customer_testing.csv")
    
    acid_test_texts = df_acid_test["UTTERANCES"].tolist()
    acid_test_labels = df_acid_test["INTENT_NAME"].tolist()
    
    columns = ["text", "intent"]    
    df_acid_train = pd.DataFrame(list(zip(acid_train_texts, acid_train_labels)), columns =columns)
    df_acid_test = pd.DataFrame(list(zip(acid_test_texts, acid_test_labels)), columns =columns)
    
    value_counts = df_acid_train['intent'].value_counts()
    value_counts = value_counts.to_dict()
    
    selectedIntents = [key for key in value_counts.keys() if value_counts[key] >= 50]
    
    df_acid_train = df_acid_train[df_acid_train.intent.isin(selectedIntents)]
    df_acid_test = df_acid_test[df_acid_test.intent.isin(selectedIntents)]

    value_counts = df_acid_train['intent'].value_counts()
    value_counts = value_counts.to_dict()
    len(value_counts)
     
    plotData(value_counts,"figures/acidData")
    
    return df_acid_train, df_acid_test

