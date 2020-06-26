import numpy as np
import maplotlib.pyplot as plt


# generate permutation sample
def permutation_sample(data1, data2):
    """generate permutation sample from two datasets"""
    data=np.concatenate(data1, data2)
    permuted_data=np.random.permutation(data)
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]
    return perm_sample_1, perm_sample_2


# visualize permutation sampling
def plot_perm_sample(data1, data2, n=50):
    perm_sample_1, perm_sample_2 = permutation_sample(data1, data2)

    def ecdf(data):
        """compute ECDF for a one-dimensional array of measurements"""
        n = len(data)
        x = np.sort(data)
        y = np.arange(1, n + 1) / n
        return x, y

    x_1, y_1 = ecdf(perm_sample_1)
    x_2, y_2 = ecdf(perm_sample_2)
    _=plt.plot(x_1, y_1, marker='.', linestyle='none', color='red', alpha=0.2)
    _=plt.plot(x_2, y_2, marker='.', linestyle='none', color='blue', alpha=0.2)

    x_1, y_1 = ecdf(data1)
    x_2, y_2 = ecdf(data2)
    _=plt.plot(x_1, y_1, marker='.', linestyle='none', color='red')
    _=plt.plot(x_2, y_2, marker='.', linestyle='none', color='blue')

    plt.margins(0.02)
    _=plt.xlabel('x')
    _=plt.ylabel('ECDF')
    plt.show()


# generate permutation replicates
def draw_perm_reps(data1, data2, func, size=1):
    """generate multiple permutation replicates"""
    perm_replicates = np.empty(size)
    for i in range(size):
        perm_sample_1, perm_sample_2 = permutation_sample(data1, data2)
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)
    return perm_replicates