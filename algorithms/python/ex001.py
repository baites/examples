import math
from heapq import *

def func(s):

    counters = {}
    for c in s:
        counters[c] = counters.setdefault(c,0) + 1

    buckets = []
    for c,f in counters.items():
        if f > math.ceil(len(s)/2.0):
            raise ValueError('No valid')
        heappush(buckets, [-f,c])

    output = []

    while len(buckets) > 0:
        f = heappop(buckets)
        output.append(f[1])
        f[0] += 1

        s = None
        if len(buckets) > 0:
            s = heappop(buckets)
            output.append(s[1])
            s[0] += 1
            if s[0] < 0:
                heappush(buckets,s)

        if f[0] < 0:
            heappush(buckets,f)

    return output

print(func(list('aaaabbcc')))
