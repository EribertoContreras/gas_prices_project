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

def state_min_wage():
    #downloading csv
    df =  pd.read_csv("Minimum Wage Data.csv",encoding='cp1252')
    return df

def fed_min_wage():
    # downloading csv
    df = pd.read_csv("MinimumWage.csv",encoding='cp1252')
    return df

def political_data():
    # downloading csv
    df = pd.read_csv("MinWage_PartyControl.csv",encoding='cp1252')
    return df 

def gas_data():
    # downloading csv
    df = pd.read_csv("PET_PRI_GND_DCUS_NUS_W.csv",encoding='cp1252')
     #making a date collumn to join gas_prices
    df['t'] = pd.to_datetime(df['Date'],format='%m/%d/%Y')
    #adding a date column with only year
    df['Year'] = df.t.dt.year
    #droppping other darte like columns to only use one.
    df = df.drop(columns = ['Date', 't'])
    return df
    
def all_gas_data():
    """ renaming functions above and merging them together so that we can have one large dataframe"""
    state_min = state_min_wage()
    fed_min = fed_min_wage()
    political_party = political_data()
    gas_prices = gas_data()

    #merging data 
    #joining state min wage with fed
    fed_state_join = state_min.merge(fed_min, how='inner')
    #joining min wage with political party
    all_plus_pol = fed_state_join.merge(political_party, how='inner')
    #merging gasprices & all_plus_political.
    update = all_plus_pol.merge(gas_prices, how='inner')
    #making all combined updated data into a DataFrame
    df = pd.DataFrame(update)
    
    return df
    

