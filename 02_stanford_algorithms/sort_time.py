import random
import time

def gen_list(exp, seed=1):
    '''
    Generates a randomly shuffled list of length "1 with 'exp' zeros".
    So, exp=3 generates a list of length 1000.
    param exp: the exponent
    param seed: the random seed to be used
    return test_list: the sorted list
    '''
    random.seed(seed)
    list_len = int(10 ** (exp-1))
    test_list = list(range(list_len))
    random.shuffle(test_list)
    return test_list


def runtime_exp(exp, func, seed):
    '''
    Times the runtime of a sorting function 
    param exp: the exponent determining the length of the function
    param func: the sorting function to be used
    param seed: the random seed to be used to sort the input list
    return run_time: the running time of the function
    '''
    start = time.time()
    func(gen_list(exp, seed=seed))
    end = time.time()
    run_time = round((end-start), 3)
    return run_time