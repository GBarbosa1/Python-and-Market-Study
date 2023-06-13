import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Declares the assets, using A, B and C here but could be AAPPL, PETR3 and so on
assets = ['A','B','B']
n = len(assets)
A = [1,2,3,2,3,4,5,6,7,1]
B = [5,6,4,7,8,7,9,6,7,8]
C = [4,5,6,5,6,7,6,5,5,5]
asset_df = pd.DataFrame([A,B,C], index = assets)
prec=asset_df.T
#Calcula retorno sobre os preços
ri = prec/prec.shift(1)-1
mi=ri.mean()
sigma=ri.cov()
###
vet_R=[]
vet_Vol=[]
for i in range(200):
    w = np.random.random(n)
    w=w/np.sum(w)
    retorno=np.sum(w*mi)
    risco = np.sqrt(np.dot(w.T,np.dot(sigma,w)))
    vet_R.append(retorno)
    vet_Vol.append(risco)
plt.plot(vet_Vol,vet_R,'ok')
plt.grid()
plt.xlabel("VOLATIDADE ESPERADA")
plt.ylabel("RETORNO ESPERADO")
plt.show()