import sys

fname = sys.argv[1]
with open(fname, 'r') as f:
    x = f.readline()
    y = x.split()
    print(x)
    print(y[0])
f.close()
