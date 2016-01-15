1#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

# in terminal: cat training | python mapper.py | sort | python reducer.py | sort | python eliminate_duplicates.py > reported_duplicates

import numpy as np
import sys

if __name__ == "__main__":
    # VERY IMPORTANT:
    # Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    
    n = 20000
    K = 40
    r = 8
    h1_a = np.random.randint(1, n, size = K)
    h1_b = np.random.randint(0, n, size = K)
    h2_a = np.random.randint(1, n, size = K)
    h2_b = np.random.randint(0, n, size = K / r)
    
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = [int(s) for s in line[16:].split()]
        
        hs = []
        b = 0
        for k in range(K):
            h = min([(h1_a[k] * s + h1_b[k]) % n for s in shingles])
            hs.append(h)
            if (k + 1) % r == 0:
                hash_value = (np.dot(h2_a[k-r+1:k+1], hs) + h2_b[b]) % n
                print '%s\t%s' % ((b, hash_value), video_id)
                hs = []
                b += 1