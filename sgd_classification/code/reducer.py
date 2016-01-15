#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import logging
import sys
import numpy as np

if __name__ == "__main__":
    w = np.zeros((1,6001))
    i = 0
    for line in sys.stdin:
        line = line.strip()
        w_i = np.fromstring(line, sep=' ')
        w = w + w_i
        i = i+1
    w = w/i
    print " ".join(str(p) for p in w[0])
