import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd 
import pandas_datareader.data as web 
import robin_stocks as rh
import json
import userFunctions as uf
import rhorders as rho

## Log in to Robinhood
uf.login()

## Get VIX
vix = uf.yahooPrice('^VIX')

## Ticker
spy = 'SPY'

## Set Min Days to Expiration
timeDeltaTarget = 5

## Get Expiration Date (Wednesday)
expirationDate = uf.wedExpiri(spy, timeDeltaTarget)

## Set Target Delta based on VIX
if vix > 20:
    delta = 0.30
else: 
    delta = 0.16

## Place Orders
uf.ironCondor(spy, expirationDate, delta, 2, 1)