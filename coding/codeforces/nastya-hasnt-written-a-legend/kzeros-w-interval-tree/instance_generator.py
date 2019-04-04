
import random

mininst = 44
maxinst = 45
maxsize = 1000
maxops = 10000
maxv = 400
minv = -maxv
maxx = 100
psum = 0.1

dir = 'tests'

for n in range(mininst, maxinst):
    size = random.randint(2, maxsize)
    size = 40000
    macv = 1000000000
    maxv =  1000000000
    minv = -1000000000
    a = [random.randint(minv,maxv) for i in range(size)]
    #a = [1 for i in range(size)]
    a.sort()
    a = [str(v) for v in a]
    with open('{}/{:04d}'.format(dir, n), 'w') as f:
        print(size, file=f)
        print(' '.join(a), file=f)
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
