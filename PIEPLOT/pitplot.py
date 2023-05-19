import matplotlib.pyplot as plt
x = ['Ação', 'Petróleo', 'Dólar', 'Comoddities', 'Títulos', 'Bitcoin']
y = [2,3,1,6,9,11]
ax=plt.subplot(111)
explodir = [0,0,0,0.2,0,0]
ax.pie(y,explode=explodir,labels=x,autopct='%1.1f%%')
plt.show()