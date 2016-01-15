import sys
import numpy as np

if __name__ == "__main__":

    if (len(sys.argv) != 2):
        raise Exception("Usage: ./build_articles.py log_file")

    # initialize article set
    articles = set()

    with file(sys.argv[1]) as inf:
        for line in inf:
            logline = line.strip().split()
            articles.update([int(x) for x in logline[9:]])

    # print all articles with random features
    for id in articles:
        line = str(id) + " " + " ".join(str(x) for x in np.random.rand(6))
        print line