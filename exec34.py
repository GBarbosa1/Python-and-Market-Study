import matplotlib.pyplot as fig
import statistics as st
import numpy as np
import pandas as pd
import scipy.stats as sci
from scipy.stats import norm
import yfinance as yf
from datetime import datetime
 
vale3 = yf.Ticker("VALE3.SA")
vale3_hist = vale3.history(start='2022-01-01',end='2023-04-21', interval= '1d')
vale3_hist.reset_index(inplace=True)

close_value = vale3_hist['Close'].to_numpy()
date = vale3_hist['Date'].to_numpy()
 
returns = (close_value[1:]-close_value[:-1])/close_value[:-1]

fig.subplot(221)
fig.plot(date,close_value)
fig.title('Vale3 diário de 01-2022 a 04-2023')

fig.subplot(222) 
fig.plot(date[1:], returns  , color = 'black')
fig.xlabel('dias')

fig.subplot(223)
fig.hist(returns, bins=50, color='gray')


fig.subplot(224)
sci.probplot(returns,dist='norm', plot=fig)
fig.title('QQ-plot Ibovespa')
fig.show()