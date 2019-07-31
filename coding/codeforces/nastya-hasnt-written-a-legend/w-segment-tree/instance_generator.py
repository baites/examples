
import random

mininst = 5
maxinst = 6
size = 100000
maxops = 50000
maxv = 1000000
#maxv = 100
minv = -maxv
maxk = 1000000
mink = -maxk
maxx = 100
psum = 0.5

dir = 'tests'

for n in range(mininst, maxinst):
    #size = random.randint(2, maxsize)
    a = [random.randint(minv,maxv) for i in range(size)]
    k = [str(0) for i in range(size-1)]
    a.sort()
    a = [str(v) for v in a]
    with open('{}/{:04d}'.format(dir, n), 'w') as f:
        print(size, file=f)
        print(' '.join(a), file=f)
        print(' '.join(k), file=f)
        print(maxops, file=f)
        for o in range(maxops):
            if random.random() <= psum:
                i = random.randint(1, size)
                x = random.randint(0, maxx)
                print('+ {} {}'.format(
                    i, x
                ), file=f)
            else:
                l = random.randint(1, size//2)
                r = random.randint(size//2+1, size)
                print('s {} {}'.format(
                    l, r
                ), file=f)
