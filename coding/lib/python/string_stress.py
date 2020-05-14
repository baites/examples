import random
import string
import time


def reffunc(a):
    return True

def testfunc(a):
    return reffun(a)


size = 100
tries = 10
alphabet = string.ascii_lowercase

agg_ref_time = 0
agg_test_time = 0

for i in range(tries):

    pop = ''.join(random.choices(alphabet, k=size))

    start = time.time()
    ref = reffunc(pop)
    ref_time = time.time()
    test = reffunc(pop)
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

print('Agg ref time {}'.format(agg_ref_time))
print('Agg test time {}'.format(agg_test_time))
print('Agg speedup x{}'.format(agg_ref_time/agg_test_time))
