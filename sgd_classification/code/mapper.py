#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import sys
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn import cross_validation
from sklearn import svm
from sklearn.kernel_approximation import RBFSampler
from sklearn.kernel_approximation import AdditiveChi2Sampler
from sklearn.grid_search import GridSearchCV


DIMENSION = 400  # Dimension of the original data.
CLASSES = (-1, +1)   # The classes that we are trying to predict.

chi_feature = AdditiveChi2Sampler(sample_steps=1)
chi_feature.fit(np.zeros([1,400]))
rbf = RBFSampler(n_components = 15*DIMENSION, random_state = 1)
rbf.fit(np.zeros([1,400]))

def transform(x_original):
    out = np.concatenate(([1], rbf.transform(chi_feature.transform(x_original)[0])[0]))
    return out

if __name__ == "__main__":
    X = []
    Y = []
    # initialize stochastic gradiant descent    
    cls = SGDClassifier(alpha = 0.0001, fit_intercept=False, n_iter = 15, penalty = "l2", warm_start = "True")
    for line in sys.stdin:
        line = line.strip()
        (label, x_string) = line.split(" ", 1)
        label = int(label)
        x_original = np.fromstring(x_string, sep=' ')
        x = transform(x_original)  # Use our features.
        X.append(x)
        Y.append(label)

    cls.fit(X, Y)
    print " ".join(str(p) for p in cls.coef_[0])
