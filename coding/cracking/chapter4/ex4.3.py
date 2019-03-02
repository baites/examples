
import math

def make_btree(s):

    ex = math.ceil(math.log(len(s)+1)/math.log(2))
    t = [None]*(2**ex-1)

    def find_root(s, i, j, n=0):
        nonlocal t
        print(i, j)
        if j - i == 1:
            return s[i]
        l = 2*n+1
        if j - i == 2:
            t[l] = s[i]
            t[n] = s[j-1]
            return t[n]
        p = (i+j)//2
        l = 2*n+1
        r = 2*n+2
        t[n] = s[p]
        t[l] = find_root(s,i,p,l)
        t[r] = find_root(s,p+1,j,r)
        return t[n]

    find_root(s, 0, len(s))
    return t

s = 'abcdef'
print(make_btree(s))
