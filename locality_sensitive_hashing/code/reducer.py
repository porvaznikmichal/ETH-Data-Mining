#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import numpy as np
import sys


def print_duplicates(videos):
    unique = np.unique(videos)
    for i in xrange(len(videos)):
        for j in xrange(i + 1, len(videos)):         
            print "%d\t%d" % (min(videos[i], videos[j]),
                              max(videos[i], videos[j]))

last_key = None
key_count = 0
duplicates = []

for line in sys.stdin:
    line = line.strip()
    key, video_id = line.split("\t")

    if last_key is None:
        last_key = key

    if key == last_key:
        duplicates.append(int(video_id))
    else:
        print_duplicates(duplicates)
        duplicates = [int(video_id)]
        last_key = key

if len(duplicates) > 0:
    print_duplicates(duplicates)
