
def solve(d, k):
    modcount = [0]*k
    for x in d:
        mod = x % k
        modcount[mod] += 1
    nboxes = 0
    for i in range(k):
        for j in range(i, k):
            if (i + j) % k != 0 or\
                modcount[i] == 0 or\
                    modcount[j] == 0:
                continue
            if i == j:
                boxes = modcount[i]//2
            else:
                boxes = min(modcount[i], modcount[j])
            modcount[i] -= boxes
            modcount[j] -= boxes
            nboxes += 2 * boxes
    return nboxes

if __name__ == "__main__":
    params = input().strip().split()
    n, k = [int(params[i]) for i in range(2)]
    d = input().strip().split()
    d = [int(d[i]) for i in range(n)]
    print(solve(d, k))
