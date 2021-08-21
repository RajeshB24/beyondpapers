import numpy as np


#### Random Splitter
def randomSplit(X,split):
    '''Randomly assigns split group'''
    idx  = np.arange(X.shape[0])
    np.random.shuffle(idx)
    idx_splits = np.array_split(idx,split)
    split_group = np.zeros(X.shape[0])
    for i in range(split):
        split_group[idx_splits[i]]=i
    return split_group

    

