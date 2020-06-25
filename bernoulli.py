import numpy as np

# Bernoulli trials
def bernoulli_trials(n,p):
    """perform n Bernoulli trials with success probability p and return number of successes"""
    n_success=0
    for i in range(n):
        random_number=np.random.random()
        if random_number < p:
            n_success += 1
    return n_success

