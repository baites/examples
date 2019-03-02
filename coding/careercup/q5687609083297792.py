
input = [(4,6), (1,2)]
#input = [(1,4), (6,8), (2,4), (7,9), (10, 15)]

def coverage(intervals):
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

print(input)
print(coverage(input))
