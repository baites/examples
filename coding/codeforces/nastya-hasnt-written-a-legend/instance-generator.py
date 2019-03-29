
import random

ninsts = 5
maxsize = 20
maxops = 30
maxv = 20
minv = -maxv
maxx = 20
psum = 0.5

dir = 'kzeros_tests'

for n in range(4, ninsts):
    size = random.randint(2, maxsize)
    a = [str(random.randint(minv,maxv)) for i in range(size)]
    a.sort()
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
                l = random.randint(1, size)
                r = random.randint(l, size)
                print('s {} {}'.format(
                    l, r
                ), file=f)
