import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
azul = pd.read_csv('SNSREGPLOT\AZUL4.SA.csv', sep=',')
petr = pd.read_csv('SNSREGPLOT\PETR4.SA.csv',sep=',')
azul_dado = azul['Close']
petr_dado = petr['Close']
sns.regplot(x = petr_dado,y = azul_dado, color='black')
plt.show()

