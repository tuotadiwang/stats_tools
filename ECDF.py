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
    _plt.margins(0.02)
    plt.show()

# plot PMF (probability mass function)
def plot_pmf(data):
    bins=np.arange(min(data),max(data)+1 +1)-0.5
    _=plt.hist(data, bins=bins, normed=True)
    _=plt.xlabel('number')
    _=plt.ylabel('PMF')
    plt.show()