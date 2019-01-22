
def do_overlap(interval, last):
    imin = interval[0]
    imax = interval[1]
    lmin = last[0]
    lmax = last[1]
    return imax >= lmin and lmax >= imin

def merge(interval, last):
    # This is why a merger needs to be mutable
    last[0] = min(last[0], interval[0])
    last[1] = max(last[1], interval[1])

def sum_intervals(intervals):
    result = 0
    for interval in intervals:
        result += interval[1] - interval[0]
    return result

def coverage(intervals):
    # Sort using interval mins as key
    intervals.sort()
    # Collection of non-overlaping intervals
    # Each merger needs to be mutable
    mergers = None
    for interval in intervals:
        if mergers is None:
            mergers = [list(interval)]
            continue
        # Correctness proof:
        # Show that checking last merger is enough
        last = mergers[-1]
        if do_overlap(interval, last):
            merge(interval, last)
        else:
            mergers.append(list(interval))
    return sum_intervals(mergers)

def coverage_naive(intervals):
    mina = 2**64
    maxb = -2**64
    for interval in intervals:
        mina = min(mina, interval[0])
        maxb = max(maxb, interval[1])
    mask = [0]*(maxb - mina)
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            mask[i-mina] = 1
    return sum(mask)

import random

while 1:

    input = []
    for n in range(100):
        imin = random.randint(0,99)
        imax = random.randint(imin+1, 100)
        input.append((imin, imax))

    print(input)
    refs = coverage_naive(input)
    test = coverage(input)
    if refs == test:
        print('OK REFS {} == TEST {}'.format(refs, test))
    else:
        break

#input = [(1,4), (6,8), (2,4), (7,9), (10, 15)]
