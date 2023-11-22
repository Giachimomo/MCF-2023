import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import argparse
import sys,os
def parse_arguments():
    parser=argparse.ArgumentParser(description='Grafici', usage='python3 Es1.py --opzione')
    parser.add_argument('--opzione1',action='store_true')
    parser.add_argument('--opzione2',action='store_true')

    return parser.parse_args()

def main():
    args=parse_arguments()
    dati=pd.read_csv('vel_vs_time.csv')
    x=dati['t']
    y=dati['v']
    distanza=[]
    for i in range(1,len(y)+1):
        distanza.append(scipy.integrate.simpson(y[:i],x=x[:i],dx=0.5))
    if args.opzione1==True:
        plt.plot(x,y)
        plt.show()
    if args.opzione2==True:
        plt.plot(x[:len(distanza)],distanza)
        plt.show()
if __name__=="__main__":
    main()

