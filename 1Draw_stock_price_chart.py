from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def company_stock(start, end, company_code):
    df = data.DataReader(company_code, 'stooq')
    df = df[(df.index>=start) & (df.index<=end)]
    
    date = df.index
    price = df['Close']
    
    span01 = 5
    span02 = 25
    span03 = 50
    
    df['sma01'] = price.rolling(window = span01).mean()
    df['sma02'] = price.rolling(window = span02).mean()
    df['sma03'] = price.rolling(window = span03).mean()
    
    plt.figure(figsize=(20, 10))
    plt.subplot(2, 1, 1)
    
    plt.plot(date, price, label = 'Close', color='#99b898')
    plt.plot(date, df['sma01'], label='sma01', color='#e84a5f')
    plt.plot(date, df['sma02'], label='sma02', color='#ff847c')
    plt.plot(date, df['sma03'], label='sma03', color='#feceab')
    plt.title(company_code, color='white', backgroundcolor='grey', size=30, loc='center')
    plt.xlabel('date', color='grey', size=20)
    plt.ylabel('price', color='grey', size=20)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.bar(date, df['Volume'], label='Volume', color='grey')
    plt.legend()
    plt.show()

start = '2019-06-01'
end = '2020-10-01'

company_stock(start, end, '4389.JP')



