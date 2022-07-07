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

# def prep_store_data(df):
#     df.sale_date = df.sale_date.apply(lambda date: date[:-13])
#     df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y')
#     # make sure we sort by date/time before resampling or doing other time series manipulations
#     df = df.set_index('sale_date').sort_index()
#     df['month'] = df.index.strftime('%m-%b')
#     df['day_of_week'] = df.index.strftime('%w-%a')
#     df['sales_total'] = df.sale_amount * df.item_price
#     return df

def prep_gas_data(df):
    # renaming collunns
    #df['fed_wage'] = df['Federal.Minimum.Wage']
     #renaming columns
    df.rename(columns = {'A1':'gasoline', 'D1': 'diesel'}, inplace = True)
    # convert our date column to datetime type
    df.set_index('Date',inplace=True)
    # adding a month column
    df['month'] = df.index.strftime('%m-%b')
    # fed info to drop
    df = df.drop(columns=['Year', 'State', 'State.Minimum.Wage',
       'State.Minimum.Wage.2020.Dollars', 'Federal.Minimum.Wage',
       'Federal.Minimum.Wage.2020.Dollars', 'Effective.Minimum.Wage',
       'Effective.Minimum.Wage.2020.Dollars', 'CPI.Average',
       'Department.Of.Labor.Uncleaned.Data',
       'Department.Of.Labor.Cleaned.Low.Value',
       'Department.Of.Labor.Cleaned.Low.Value.2020.Dollars',
       'Department.Of.Labor.Cleaned.High.Value',
       'Department.Of.Labor.Cleaned.High.Value.2020.Dollars', 'Footnote',
       'FederalMinimumWage', 'MeanAnnualInflation',
       'MinWageIndexedLastRaiseYear', 'UnemploymentRateDecember',
       'GDP_AnnualGrowth', 'PresParty', 'SenParty', 'HouseParty',
       'TrifectaFlag', 'FedMinWage', 'RateChange', 'PercentChange',
       'IncreaseFlag', 'YearsSinceLastChange', 'A2', 'A3', 'R1',
       'R2', 'R3', 'M1', 'M2', 'M3', 'P1', 'P2', 'P3'])
 
   
    return df


                        