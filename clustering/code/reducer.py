#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np
from sklearn.cluster import MiniBatchKMeans

# parameters
batch_size = 750

# initialize mini batch k-means
mbk = MiniBatchKMeans(n_clusters = 100, batch_size = batch_size, n_init = 20)
counter = 0
X = []
for line in sys.stdin:
    counter += 1
    key, data = line.strip().split('\t')
        
    for centroid in data.split(','):
        point = np.array([float(x) for x in centroid.split(' ')])
        X.append(point)

    if counter % batch_size == 0:
        # partial fit
        X = np.array(X)
        mbk.partial_fit(X)
        X = []

# fit the last batch
if X != []:
    X = np.array(X)
    mbk.partial_fit(X)


# get cluster centers
clusters = mbk.cluster_centers_
for centroid in clusters:
    print " ".join(str(x) for x in centroid)



