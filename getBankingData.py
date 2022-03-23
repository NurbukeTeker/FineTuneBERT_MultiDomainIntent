# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:18:46 2022

@author: nurbuketeker
"""
import pandas as pd
from plotDataset import plotData

def getBankingData():
    df_banking_train = pd.read_csv("BankingData/train.csv")
    
    banking_train_texts = df_banking_train["text"].tolist()
    banking_train_labels = df_banking_train["category"].tolist()
    
    df_banking_test = pd.read_csv("BankingData/test.csv")
    
    banking_test_texts = df_banking_test["text"].tolist()
    banking_test_labels = df_banking_test["category"].tolist()
    
    columns = ["text", "intent"]    
    df_banking_train = pd.DataFrame(list(zip(banking_train_texts, banking_train_labels)), columns =columns)
    df_banking_test = pd.DataFrame(list(zip(banking_test_texts, banking_test_labels)), columns =columns)
    
    value_counts = df_banking_train['intent'].value_counts()
    value_counts = value_counts.to_dict()
    
    selectedIntents = [key for key in value_counts.keys() if value_counts[key] >= 50]
    
    df_banking_train = df_banking_train[df_banking_train.intent.isin(selectedIntents)]
    df_banking_test = df_banking_test[df_banking_test.intent.isin(selectedIntents)]

    value_counts = df_banking_train['intent'].value_counts()
    value_counts = value_counts.to_dict()
    len(value_counts)
     
    plotData(value_counts,"figures/bankingData")
    
    return df_banking_train ,df_banking_test
    
