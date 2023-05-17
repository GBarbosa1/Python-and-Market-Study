import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
btcdado = pd.read_csv('BTC-USD.csv', sep=',')
btcdado_np = btcdado['Close'].to_numpy()
return_btc = (btcdado_np[1:]-btcdado_np[:-1])/btcdado_np[:-1]
print(return_btc)
sns.boxplot(data=return_btc)
plt.show()

