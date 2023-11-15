import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import reco
dati=pd.read_csv('hit_times_M0.csv')
print (dati.columns)
'''
x=dati['hit_time']
y=dati['det_id']
plt.hist(x,bins=100,range=[200000,1000000000])
plt.show()
diff=np.diff(x)
mask=diff>0
log=np.log10(diff[mask])
plt.hist(log,bins=100)
plt.show()
'''
modulo=dati['mod_id'].values
sensore=dati['det_id'].values
tempo=dati['hit_time'].values
recohit=[]
for i in range(len(modulo)):
    x=reco.hit(modulo[i],sensore[i],tempo[i])
    recohit.append(x)
array=np.array(recohit)
ordinato=np.sort(array)
print(ordinato)
differenza=np.diff(ordinato)
print(differenza)
plt.hist(differenza, bins=100,range=(0,100) )
plt.show()
