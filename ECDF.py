import numpy as np
import matplotlib.pyplot as plt

# compute ECDF (Emipirical cumulative distribution function)
def ecdf(data):
    """compute ECDF for a one-dimensional array of measurements"""
    n=len(data)
    x=np.sort(data)
    y=np.arange(1,n+1)/n
    return x,y

# plot ECDF
def plot_ecdf(x,y,xlabel):
    _=plt.plot(x,y,marker='.',linestyle='none')
    _=plt.xlabel(xlabel)
    _=plt.ylabel('ECDF')
    plt.show()