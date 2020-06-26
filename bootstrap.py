import numpy as np
import matplotlib.pyplot as plt

# bootstrap replicate function
def bootstrap_replicate_1d(data, func):
    """1D array"""
    bs_sample=np.random.choice(data, len(data))
    return func(bs_sample)

# generate many bootstrap replicates
def draw_bs_reps(data, func, size=1):
    bs_replicates = np.empty(size)
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)
    conf_int =np.percentile(bs_replicates, [2.5, 97.5])
    print('95% confidence interval=',conf_int)
    return bs_replicates

# pairs bootstrap
def draw_bs_pairs_linreg(x,y,size=1):
    """pairs bootstrap for linear regression"""
    inds = np.arange(len(x))
    bs_slope_reps=np.empty(size)
    bs_intercept_reps=np.empty(size)
    for i in range(size):
        bs_inds=np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x,bs_y,1)
        return bs_slope_reps, bs_intercept_reps


