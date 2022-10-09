# Chryzal Beaudelaire ZOSSOU 2022
# Performance Profiles for Machine Learning Python library
# Author: Chryzal Beaudelaire ZOSSOU <bchryzal@gmail.com>
#
# License: MIT

import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# Create PPML Folder
PPML_DIR = './ppml'

try:
    os.mkdir(PPML_DIR)
except:
    print('')

def graph_plot(df, filename='ppml_plot', max_x=None):
    if df.shape[0] < 1:
        return print('Data not found')

    nbInstances = len(df.index)

    dfT = np.transpose(df)

    ratio = pd.DataFrame()
    for v in dfT:
        ratio[v] = dfT[v]/dfT[v].min()
    
    ratio = np.transpose(ratio)


    x = []
    for v in ratio:
        x += ratio[v].unique().tolist()

    x = list(dict.fromkeys(x))
    x.sort()

    y = {}
    for v in df:
        y[v] = []

    def countValue(dflist, value):
        counter = 0
        for v in dflist:
            if v == value:
                counter += 1
        return counter

    for i in x:
        for v in df:
            c = countValue(ratio[v], i)
            y[v].append(c)
        
    for v in df:
        y[v] = np.cumsum(y[v])/nbInstances
        
    # Get the maximum's x 
    max_x = np.max(x)+.02 if max_x==None else max_x
    
    fontT = {'family':'serif','color':'darkred','size':15}
    plt.figure(figsize=(14, 7))
    plt.title(f'{filename}', fontdict = fontT)
    plt.xlabel("Taux")
    plt.ylabel('% instances')
    plt.xlim(0, max_x)
    plt.grid()

    for v in df:
        plt.plot(x, y[v], label = v)
    plt.legend()

    plt.savefig(f'{PPML_DIR}/{filename}.pdf')
    plt.show()

def mae(y_true, y_predict):
    maes=[]
    for v, t in zip(y_predict, y_true):
        k = np.abs(v-t)
        if k==0:
            k=0.001
        maes.append(k)
    return maes

def PPMLRegressor(df, target=None, filename='ppml_plot'):

    if df.shape[0] < 1:
        return print('Data not found')

    if target == None:
        return print('Target column not specified')

    models = [col for col in df.columns if str(col) != target]

    ppml_df = pd.DataFrame()
    for model in models:
        ppml_df[model] = mae(df[target], df[model])

    # Save Err data
    ppml_df.to_csv(f'{PPML_DIR}/ppml_mae.csv', index_label=False, index=False)

    return graph_plot(ppml_df, filename)
    