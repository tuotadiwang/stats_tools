import numpy as np
import matplotlib.pyplot as plt

# successive poisson
def sucessive_poisson(tau1, tau2, size):
    """combined waiting time for two successive rare events"""
    t1 = np.random.exponential(tau1, size)
    t2 = np.random.exponential(tau2, size)

    _=plt.hist(t1+t2, bins=100, normed=True)
    _=plt.xlabel('waiting time')
    _=plt.ylabel('PDF')
    plt.show()

    return t1+t2