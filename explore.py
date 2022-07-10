# coding 
import math
from math import sqrt
import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import scipy.stats
import scipy
import os

# needed for modeling
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer
from sklearn.metrics import explained_variance_score
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (16,9)
plt.rcParams["font.size"] = 20
import requests
from statsmodels.tsa.api import Holt
import requests
import acquire

def split_data(df):
    df_resampled = df.resample('6w')[['gasoline','diesel']].mean()
    # set train size to be 50% of total 
    train_size = int(round(df_resampled.shape[0] * 0.5))
    # set validate size to be 30% of total 
    validate_size = int(round(df_resampled.shape[0] * 0.5))
    # set test size to be number of rows remaining. 
    test_size = int(round(df_resampled.shape[0] * 0.0))
    # validate
    validate_end_index = train_size + validate_size
    validate_end_index
    # train 
    train = df_resampled[:train_size]
    # validate 
    validate = df_resampled[train_size:validate_end_index]
    # test
    test = df_resampled[validate_end_index:]
    return train, validate, test
    
def evaluate(target_var):

    '''
    This function will take the actual values of the target_var from validate, 
    and the predicted values stored in yhat_df, 
    and compute the rmse, rounding to 0 decimal places. 
    it will return the rmse. 
    '''
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0)
    return rmse

def plot_and_eval(target_var):
    '''
    This function takes in the target var name (string), and returns a plot
    of the values of train for that variable, validate, and the predicted values from yhat_df. 
    it will als lable the rmse. 
    '''
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var])
    plt.plot(validate[target_var])
    plt.plot(test[target_var])
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    #rmse = evaluate(target_var)
    #print(target_var, '-- RMSE: {:.0f}'.format(rmse))
    plt.show()
    
    # create an empty dataframe
    eval_df = pd.DataFrame(columns=['model_type', 'target_var', 'rmse'])

# function to store the rmse so that we can compare
def append_eval_df(model_type, target_var):
    '''
    this function takes in as arguments the type of model run, and the name of the target variable. 
    It returns the eval_df with the rmse appended to it for that model and target_var. 
    '''
    rmse = evaluate(target_var)
    d = {'model_type': [model_type], 'target_var': [target_var],
        'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)

    
def viz1(train):
    y = train.gasoline
    plt.figure(figsize=(12,10))
    y.plot(alpha=.2, label='hourly')
    y.resample('15D').mean().plot(alpha=0.5, label='15-Day')
    y.resample('6w').mean().plot(alpha=0.8, label='6-Week')
    y.resample('6M').mean().plot(label='6-Month')
    y.resample('Y').mean().plot(label='Yearly',  xlabel=' ',
                                            ylabel='Percent(%) Change')
    plt.legend()

def viz2(validate):
    y = validate.gasoline
    plt.figure(figsize=(12,10))
    y.plot(alpha=.2, label='hourly')
    y.resample('15D').mean().plot(alpha=0.5, label='15-Day')
    y.resample('6w').mean().plot(alpha=0.8, label='6-Week')
    y.resample('6M').mean().plot(label='6-Month')
    y.resample('Y').mean().plot(label='Yearly',  xlabel=' ',
                                            ylabel='Percent(%) Change')
    plt.legend()

def viz3(test):
    y = test.gasoline
    plt.figure(figsize=(12,10))
    y.plot(alpha=.2, label='hourly')
    y.resample('15D').mean().plot(alpha=0.5, label='15-Day')
    y.resample('6w').mean().plot(alpha=0.8, label='6-Week')
    y.resample('6M').mean().plot(label='6-Month')
    y.resample('Y').mean().plot(label='Yearly',  xlabel=' ',
                                            ylabel='Percent(%) Change')
    plt.legend()

def viz4(df):
    y = df.gasoline
    plt.figure(figsize=(10,8))
    y.resample('6w').mean().diff().plot(title='Volitility of the gas price % Change Over a 6 week Time period', xlabel= ' ')

def viz5(train):
    #adding a month collum to train
    train['month'] = train.index.strftime('%m-%b')
    #creating a boxpolot to vizualize train
    sns.boxplot(train.month, y = train.gasoline)
