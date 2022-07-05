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
    df['state_wage'] = df['State.Minimum.Wage']
    df['fed_wage'] = df['Federal.Minimum.Wage']
    # fed info to drop
    df = df.drop(columns=['Effective.Minimum.Wage','Federal.Minimum.Wage','FedMinWage','RateChange','IncreaseFlag','PercentChange','TrifectaFlag'])
    #dropping gas collumns that are not needed.
    df = df.drop(columns=['A2','A3','R2','R3','M2','M3','P2','P3','R1','M1','P1'])
    #state info to drop
    df = df.drop(columns=['State.Minimum.Wage.2020.Dollars',
                            'Federal.Minimum.Wage.2020.Dollars',
                            'Effective.Minimum.Wage.2020.Dollars',
                            'CPI.Average',
                            'Department.Of.Labor.Uncleaned.Data',
                            'Department.Of.Labor.Cleaned.Low.Value',
                            'Department.Of.Labor.Cleaned.Low.Value.2020.Dollars',
                            'Department.Of.Labor.Cleaned.High.Value',
                            'Department.Of.Labor.Cleaned.High.Value.2020.Dollars',
                            'Footnote','MinWageIndexedLastRaiseYear','FederalMinimumWage'])
    #renaming columns
    df.rename(columns = {'A1':'gasoline', 'D1':'diesel'}, inplace = True)
    # convert our date column to datetime type
    df.set_index('Date',inplace=True)
    # adding a month column
    df['month'] = df.index.strftime('%m-%b')
    # creating columns to refelct the difference using division from the gas types and the wage minimuns
    df['gas_fed_min_dif'] = df.gasoline / df.fed_wage
    df['gas_state_min_dif'] = df.gasoline / df.state_wage
    df['diesel_fed_min_dif'] = df.diesel / df.fed_wage
    df['diesel_state_min_dif'] = df.diesel / df.state_wage
    df = df[(df.diesel_state_min_dif >= 0.15495934959349592)&(df.replace([np.inf, -np.inf], np.nan).notnull().all(axis=1))&
            ( df['State.Minimum.Wage'] >= 4.300000)]
    return df


                        