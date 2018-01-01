import random

def random_range(n, seed):
    random.seed(123117)
    return random.sample(range(100), 100)