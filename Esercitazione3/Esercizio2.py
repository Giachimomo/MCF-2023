import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dati=pd.read_csv('4LAC_DR2_sel.csv')
print(dati.columns)
print(dati)
y=dati['PL_Index']
x=dati['Flux1000']
'''plt.scatter(x,y)
plt.show()
plt.scatter(x,y)
plt.xscale('log')
plt.show()'''

logs=dati.loc[(dati['nu_syn']>0)]
x2=np.log(logs['nu_syn'])
y2=logs['PL_Index']
'plt.scatter(x2,y2)'
'plt.show()'

bll=logs.loc[(logs['CLASS']=='bll')]
fsrq=logs.loc[(logs['CLASS']=='fsrq')]
x3=np.log(bll['nu_syn'])
x4=np.log(fsrq['nu_syn'])
y3=bll['PL_Index']
y4=fsrq['PL_Index']
plt.scatter(x3,y3,alpha=0.5)
plt.scatter(x4,y4,alpha=0.7)
plt.show()
plt.scatter(x3,y3,alpha=0.5)
plt.scatter(x4,y4,alpha=0.7)
plt.errorbar(x3,y3,yerr=bll['Unc_PL_Index'],alpha=0.5)
plt.errorbar(x4,y4,yerr=fsrq['Unc_PL_Index'],alpha=0.5)
plt.show()

n,bis,p=plt.hist(bll['PL_Index'],bins=100,alpha=0.5)
n,bis,p=plt.hist(fsrq['PL_Index'],bins=100,alpha=0.5)
plt.show()
n,bis,p=plt.hist(x3,bins=100,alpha=0.5)
n,bis,p=plt.hist(x4,bins=100,alpha=0.5)
plt.show()
