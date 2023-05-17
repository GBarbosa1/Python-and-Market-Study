import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
dolar = pd.read_csv('DX=F.csv',sep=',')
bitcoin = pd.read_csv('BTC-USD.csv',sep=',')
dolar_fechamento = dolar['Close'].to_numpy().astype(float)
bitcoin_fechamento = dolar['Close'].to_numpy().astype(float)
beta,beta0,r_value,p_value,std_err=stats.linregress(dolar_fechamento,bitcoin_fechamento)
yLin = beta*dolar_fechamento + beta0
plt.plot(dolar_fechamento,yLin,'-k',dolar_fechamento,bitcoin_fechamento,'ok')
plt.show()