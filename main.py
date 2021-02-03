import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import os
import math as m
import seaborn as sn
import GPy
import sys 
from utils import train_step
import pandas as pd 
from itertools import chain
import itertools
import pickle 
import contextlib
import functools
import time
import scipy 
import tensorflow as tf 
from changepoint import *
from training import *
from search import *






if __name__ =="__main__" :
    Y = np.array(pd.read_csv("./data/105.csv")["x"])[:500].reshape(-1, 1)
    X = np.linspace(0,len(Y),len(Y)).reshape(-1,1)
    plt.plot(Y)
    plt.show()
    X_s = np.linspace(0,len(Y)+20,len(Y)+20).reshape(-1, 1)
    t0 = time.time()
    model,kernel= launch_analysis(X,Y,X_s,straigth=True,do_plot=True,depth=2,verbose=True,initialisation_restart=10,reduce_data=False,experimental_multiprocessing=True) #straight parameters == True
    print('time took: {} seconds'.format(time.time()-t0))
    model.describe(kernel)
    mu,cov = model.predict(X,Y,X_s,kernel)
    model.decompose(kernel,X,Y,X_s)
    plt.show()
