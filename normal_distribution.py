import numpy as np
import matplotlib.pyplot as plt

# check normality
def check_normality(data):
    mu=np.mean(data)
    sigma=np.std(data)
    samples=np.random.normal(mu, sigma,size=10000)

    def ecdf(data):
        """compute ECDF for a one-dimensional array of measurements"""
        n = len(data)
        x = np.sort(data)
        y = np.arange(1, n + 1) / n
        return x, y

    x,y=ecdf(data)
    x_theor, y_theor = ecdf(samples)

    _=plt.plot(x_theor, y_theor)
    _=plt.plot(x,y, marker='.',linestyle='none')
    _=plt.xlabel('x')
    _=plt.ylabel('CDF')
    plt.show()


# probability with normal distribution
def normal_proba(data, x, size=100000):
    """probability of data <= x"""
    mu = np.mean(data)
    sigma = np.std(data)
    samples = np.random.normal(mu, sigma, size)
    proba=np.sum(samples <= x)/size
    return proba