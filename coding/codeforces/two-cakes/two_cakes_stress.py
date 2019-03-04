# http://codeforces.com/problemset/problem/1130/B

from sortedcontainers import SortedDict

def reffunc(array, size):
    houses = {}
    for i in range(size):
        tier = array[i]
        houses.setdefault(tier, []).append(i)
    dist = 0
    oldsasha = 0
    olddima = 0
    for key in sorted(houses.keys()):
        sasha, dima = houses[key]
        dist += abs(sasha - oldsasha) +\
                abs(dima - olddima)
        oldsasha = sasha
        olddima = dima
    return dist


def testfunc(array, size):
    houses = SortedDict()
    for i in range(size):
        tier = array[i]
        houses.setdefault(tier, []).append(i)
    dist = 0
    oldsasha = 0
    olddima = 0
    for key in houses.keys():
        sasha, dima = houses[key]
        dist += abs(sasha - oldsasha) +\
                abs(dima - olddima)
        oldsasha = sasha
        olddima = dima
    return dist


import random
import time

tries = 10
size = 100000

agg_ref_time = 0
agg_test_time = 0

for i in range(tries):

    array = list(range(1, size+1))
    array += array
    #random.shuffle(array)
    array.sort()

    start = time.time()
    ref = reffunc(array, len(array))
    ref_time = time.time()
    test = testfunc(array, len(array))
    test_time = time.time()
    speedup = (ref_time - start)/\
                (test_time - ref_time)
    agg_ref_time += ref_time - start
    agg_test_time += test_time - ref_time

    if test == ref:
        print('test = {}, ref = {} (x{})'.format(
            test, ref, speedup
        ))
        print('ok')
    else:
        print(pop)
        print('test = {}, ref = {}'.format(
            test, ref
        ))
        print('bad')
        break

print('Avg ref time {}'.format(agg_ref_time/4))
print('Avg test time {}'.format(agg_test_time/4))
print('Agg speedup x{}'.format(agg_ref_time/agg_test_time))
