import sys
import yfinance as yf
import pandas as pd
import matplotlib as plt
from datetime import datetime
#plt.style.use('seaborn')

tickers = 'AAPL'

# tickers = input("ticker please:")

def analysisout (tickers, period='5y', interval='1d'):
    stock = yf.Ticker(tickers)
    stockinfo = stock.info
    twohundred = stock.info['twoHundredDayAverage']
    volume = stock.info['volume']
    recs = stock.recommendations
    lastClose = stock.info['previousClose']
    percentBelow200 = (lastClose - twohundred) / twohundred * 100

    hist = stock.history(period, interval)

    hist.reset_index(inplace=True)
    hist = hist.rename(columns={'index': 'Date', 'Close':'Price'})
    hist = hist[['Date', 'Price', 'Volume']]

    return (hist)

    # return({'Short Name':stock.info.get('shortName'),
    #         "Two Hundred Day Price:": twohundred,
    #         "Previous Close Price:": stock.info.get('previousClose'),
    #         "Percent Difference:": percentBelow200,
    #         "Volume:": volume})
    # print(stockinfo.keys())
    # return()
# pd.set_option('display.max_columns',None)
print(analysisout(tickers))

# PDAnalasis = pd.DataFrame(analysisout(tickers))
# print(type(PDAnalasis))
#for key,value in stockinfo.items():
    #print(key,":",value)



