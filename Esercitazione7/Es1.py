import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
dati=pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')
print(dati.columns)
massa_invariante=[]
for i in range (len(dati['Run'])):
                mi=np.sqrt(np.power(dati['E1'][i]+dati['E2'][i],2)-(np.power(dati['px1'][i]+dati['px2'][i],2)+np.power(dati['py1'][i]+dati['py2'][i],2)+np.power(dati['pz1'][i]+dati['pz2'][i],2)))
                massa_invariante.append(mi)
n,bins,p=plt.hist(massa_invariante,bins=100,range=[2.9,3.3])
plt.show()
values=(bins[:-1]+bins[1:])/2
m=np.sum(massa_invariante)/len(massa_invariante)
p=0
for i in range(len(massa_invariante)):
    r=np.power(massa_invariante[i]-m,2)
    p=p+r
o=np.sqrt(p/len(massa_invariante))
def fit1(x,m,o,A,p1,p0):
    return(A*np.exp(-np.power((x-m),2)/(2*o*o))+p1*x+p0)
params, params_covariance = optimize.curve_fit(fit1,values,n,sigma=np.sqrt(n),absolute_sigma=True)
print(params)

ytry=fit1(values,params[0],params[1],params[2],params[3],params[4])
scarto=ytry-n
fig,ax=plt.subplots(3,1)
ax[0].plot(values,ytry)
ax[0].hist(massa_invariante,bins=100,range=[2.9,3.3])
ax[1].errorbar(values,scarto,fmt='o',yerr=np.sqrt(n))
ax[1].axhline(0,color='r')
ax[2].errorbar(values,scarto/np.sqrt(n),fmt='o')
ax[2].axhline(0,color='r')
plt.show()
plt.hist(scarto/np.sqrt(n),bins=20)
plt.show()

chi2=np.sum((ytry-n)**2/ytry)
print(chi2)
sigmaa=np.sqrt(params_covariance[0][0])
print ('Prima massa = ',params[0],'+-',sigmaa)
print('Seconda Parte')
def fit2(x,m,o1,o2,A1,A2,p1,p0):
                return(A1*np.exp(-np.power(x-m,2)/(2*o1*o1))+A2*np.exp(-np.power(x-m,2)/(2*o2*o2))+x*p1+p0)
params1,params_covariance1=optimize.curve_fit(fit2,values,n,sigma=np.sqrt(n),absolute_sigma=True)
print(params1)
ytry1=fit2(values,params1[0],params1[1],params1[2],params1[3],params1[4],params1[5],params1[6])
scarto1=ytry1-n
fig1,ax1=plt.subplots(3,1)
ax1[0].plot(values,ytry1)
ax1[0].hist(massa_invariante,bins=100,range=[2.9,3.3])
ax1[1].errorbar(values,scarto1,fmt='o',yerr=np.sqrt(n))
ax1[1].axhline(0,color='r')
ax1[2].errorbar(values,scarto1/np.sqrt(n),fmt='o')
ax1[2].axhline(0,color='r')
plt.show()
plt.hist(scarto/np.sqrt(n),bins=20)
plt.show()
chi21=np.sum((ytry1-n)**2/ytry1)
print(chi21)
sigmaa1=np.sqrt(params_covariance1[0][0])
print('Seconda massa = ',params1[0],'+-', sigmaa1)
