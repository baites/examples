import random
from solution import solve

size = 100000
minv = 1000
maxv = 10**9

if __name__ == "__main__":
    k = 100
    d = [random.randint(minv,maxv) for i in range(size)]
    print(solve(d, k))
