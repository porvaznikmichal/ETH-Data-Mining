import sys

if __name__ == "__main__":
    X = []
    Y = []
    for line in sys.stdin:
        line = line.strip()
        (label, x_string) = line.split(" ", 1)
        X.append(x_string)
        Y.append(label)

    print "\n".join(p for p in Y)