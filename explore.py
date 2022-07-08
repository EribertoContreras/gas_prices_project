from cgi import test
from lib2to3.pgen2.pgen import DFAState
from lib2to3.refactor import get_all_fix_names
import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import scipy
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')
import requests
import acquire

def viz1(df):
    for col in df.columns:
    #graph size
    plt.figure(figsize=(4,2))
    #histogram graph
    plt.hist(df[col])
    #title of column
    plt.title(col)
    # show graph
    plt.show()

def viz1(df):
    plt.figure(figsize=(12,10))
    df.plot(alpha=.2, label='hourly')
    df.resample('15D').mean().plot(alpha=0.5, label='15-Day')
    df.resample('6w').mean().plot(alpha=0.8, label='6-Week')
    df.resample('6M').mean().plot(label='6-Month')
    df.resample('Y').mean().plot(label='Yearly',  xlabel=' ', ylabel='Percent(%) Change')
    plt.legend()