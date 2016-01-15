#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np
from sklearn.cluster import MiniBatchKMeans

# parameters
batch_size = 750

# initialize mini batch k-means
mbk = MiniBatchKMeans(n_clusters = 750, batch_size = batch_size, n_init = 50)

# read the data
X = []
counter = 0
for line in sys.stdin:
    point = np.array([float(x) for x in line.strip().split()]) 
    X.append(point)
    counter += 1
    if counter % batch_size == 0:
        X = np.array(X)
        # fit batch
        mbk.partial_fit(X)
        # reset X
        X = []

# fit the last batch
if X != []:
    X = np.array(X)
    mbk.partial_fit(X)


clusters = mbk.cluster_centers_
print '0\t' + ",".join(" ".join(str(x) for x in cluster) for cluster in clusters)
