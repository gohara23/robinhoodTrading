import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd 
import pandas_datareader.data as web 
import robin_stocks as rh
import json
import userFunctions as uf
import rhorders as rho
from yahoo_fin import options
from yahoo_fin import stock_info as si 

spy_tickers = si.tickers_sp500()
spy_tickers.append('SPY')
spy_tickers.append('TLT')
print(spy_tickers)
# scrape the options data for each Dow ticker
spy_data = {}
for ticker in spy_tickers:
    ticker_dates= options.get_expiration_dates(ticker)
    info = {} 
    for date in ticker_dates:
        info[date] = options.get_options_chain(ticker)
        pd.DataFrame.to_csv('{}{}.csv'.format(ticker,date))

