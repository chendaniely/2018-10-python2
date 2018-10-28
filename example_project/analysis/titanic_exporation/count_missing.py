from pandas import isna
from numpy import sum

def count_missing(vec):
    """Count the number of missing values in a vector
    """
    #print('hello')
    null_vec = isna(vec)
    return sum(null_vec)
