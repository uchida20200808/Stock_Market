from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib as ta
import warnings
warnings.simplefilter('ignore')

def company_stock(start, end, company_code):
    df = data.DataReader(company_code, 'yahoo')
    df = df[(df.index>=start) & (df.index<=end)]
    
    date = df.index
    close = df['Adj Close']
    
            
    span01 = 5
    span02 = 25
    span03 = 50
    
    df['sma01'] = close.rolling(window = span01).mean()
    df['sma02'] = close.rolling(window = span02).mean()
    df['sma03'] = close.rolling(window = span03).mean()
    df['macd'], df['macdsignal'], df['macdhist'] = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    df['RSI'] = ta.RSI(close, timeperiod=span02)
    df["upper"], df["middle"], df["lower"] = ta.BBANDS(close, timeperiod=span02, nbdevup=2, nbdevdn=2, matype=0)
    
    plt.figure(figsize=(30, 15))
    plt.subplot(5, 1, 1)
    plt.plot(date, close, label = 'Close', color='#99b898')
    plt.plot(date, df['sma01'], label='sma01', color='#e84a5f')
    plt.plot(date, df['sma02'], label='sma02', color='#ff847c')
    plt.plot(date, df['sma03'], label='sma03', color='#feceab')
    plt.legend()
    
    plt.subplot(5, 1, 2)
    plt.bar(date, df['Volume'], label='Volume', color='grey')
    plt.legend()
    
    plt.subplot(5, 1, 3)
    plt.fill_between(date, df['macdhist'], label='MACD_hist', color='grey', alpha=0.5)
    plt.hlines(0, start, end, "grey", linestyles="dashed")
    plt.legend()
    
    plt.subplot(5, 1, 4)
    plt.plot(date, df['RSI'], label='RSI', color="grey")
    plt.ylim(0, 100)
    plt.hlines([30, 50, 70], start, end, "grey", linestyles="dashed")
    plt.legend()
    
    plt.subplot(5, 1, 5)
    plt.plot(date, close, label='Close', color='#99b898')
    plt.fill_between(date, df["upper"], df["lower"], color="grey", alpha=0.3)
    plt.legend()
    
    #plt.title(company_code, color='white', backgroundcolor='grey', size=30, loc='center')
    #plt.xlabel('date', color='grey', size=20)
    #plt.ylabel('price', color='grey', size=20)
    #plt.legend()
    
    plt.show()
    
    
start = '2019-10-01'
end = '2020-10-01'

company_stock(start, end, 'BTC-JPY')



