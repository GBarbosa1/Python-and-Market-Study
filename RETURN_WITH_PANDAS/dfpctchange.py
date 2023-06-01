import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

btcdado = pd.read_csv('RETURN_WITH_PANDAS\BTC-USD.csv', sep=',')
btcdado_returns=btcdado['Close'].pct_change(1)
print(btcdado_returns)
plt.hist(btcdado_returns)
plt.show()

