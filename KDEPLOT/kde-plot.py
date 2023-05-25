import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
nvdado = pd.read_csv(r"KDEPLOT\NVDA.csv", sep=',')
nvdado_np = nvdado['Close'].to_numpy()
date_np=nvdado['Date'].to_numpy()
date_np=np.asarray(date_np, dtype=np.datetime64)
return_nvd = (nvdado_np[1:]-nvdado_np[:-1])/nvdado_np[:-1]
plt.subplot(211)
plt.plot(date_np,nvdado_np)
plt.subplot(212)
cmap = sns.cubehelix_palette(8,start=0,light=1,as_cmap=True)
sns.kdeplot(x=date_np,y=nvdado["Close"],cmap=cmap,fill=True)
plt.show()

