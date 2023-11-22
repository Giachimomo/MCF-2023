import scipy 
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys,os
def parse_arguments():
    parser=argparse.ArgumentParser(description='Potenziali',usage='python3 Es2.py --opzione')
    parser.add_argument('--Potenziale6',action='store_true')
    parser.add_argument('--Potenziale2',action='store_true')
    return parser.parse_args()
def main():
    args=parse_arguments()
    xx = np.arange(-5,5.05, 0.1)
    m=0.5
    xxr=xx[xx>=0]
    if args.Potenziale6==True:
        x0=4.5
        plt.plot(xx, 0.1*xx**6, color='slategray')
        plt.axvline(color='k', linewidth=0.5)
        plt.xlabel('x')
        plt.ylabel(r'V(x)')
        plt.plot(x0, 0.1*x0**6, 'o', markersize=12, color='tomato')
        plt.show()
        V=0.1*xxr**6
        v0=0.1*xxr**6
        periodo=[]
        for i in range(3,len(xxr)+1):
           # v0=0.1*xxr[i-1]**6
            integrale=scipy.integrate.simpson(1/np.sqrt(v0[i-1]-V[:i-1]),x=xxr[:i-1],dx=0.1)
            a=np.sqrt(8*m)*integrale
            periodo.append(a)
            print(a)
        plt.plot(periodo,xxr[:len(periodo)])
        plt.show()
    if args.Potenziale2==True:
        plt.plot(xx, 0.1*xx**2, color='slategray')
        plt.axvline(color='k', linewidth=0.5)
        plt.xlabel('x')
        plt.ylabel(r'V(x)')
        plt.plot(x0, 0.1*x0**2, 'o', markersize=12, color='tomato')
        plt.show()
        V=0.1*xxr**2
        periodo=[]
        for i in range(2,len(xxr)-1):
            v0=0.1*xxr[i-1]**2
            integrale=scipy.integrate.simpson(1/np.sqrt(v0-V[:i-1]),x=xxr[:i-1],dx=0.1)
            a=np.sqrt(8*m)*integrale
            periodo.append(a)
            print(a)
        plt.plot(periodo,xxr[:len(periodo)])
        plt.show()
if __name__=="__main__":
    main()



