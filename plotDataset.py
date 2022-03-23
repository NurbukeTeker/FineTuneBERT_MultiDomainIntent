# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:28:48 2022

@author: nurbuketeker
"""

import matplotlib.pyplot as plt

def plotData(value_counts,filename):
    
    # Data to plot
    labels = []
    sizes = []
    
    for x, y in value_counts.items():
        labels.append(x)
        sizes.append(y)
    
    # Plot
    plt.pie(sizes, labels=labels)
    
    plt.axis('equal')
    plt.show()
    plt.savefig(filename)