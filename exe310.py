import pandas as pd
import matplotlib.pyplot as fig
import numpy as np
from scipy import stats

def returns(closing):
    returns_over_asset = (closing[1:]-closing[:-1])/closing[:-1]
    return returns_over_asset
    
vale3 = pd.read_csv('vale3.csv',sep=',')
petr4 = pd.read_csv('petr4.csv',sep=',')
ibov = pd.read_csv('ibov.csv',sep=',')
vale3 = vale3.apply(lambda x: x.str.replace(',','.'))
petr4 = petr4.apply(lambda x: x.str.replace(',','.'))
petr4 = petr4.apply(lambda x: x.str.replace(',','.'))

vale3_fechamentos = vale3['FECHAMENTO'].to_numpy().astype(float)
retorno_vale = returns(vale3_fechamentos)
petr_fechamentos = petr4['FECHAMENTO'].to_numpy().astype(float)
retorno_petr = returns(petr_fechamentos)

print(stats.ttest_ind(retorno_vale,retorno_petr))
fig.subplot(311)
fig.plot(retorno_petr,'-k')
fig.title('Retorno petr')
fig.subplot(312)
fig.title('Retorno petr')
fig.plot(retorno_petr,'-k')
ax = fig.subplot(313)
ax.boxplot([retorno_petr,retorno_vale],showfliers=False)
ax.set_xticklabels(['PETR4','VALE3'])
fig.show()
