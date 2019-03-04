# http://codeforces.com/problemset/problem/1130/B

def solve(array, size):
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


if __name__ == "__main__":
    size = int(input().strip())
    array = input().strip().split()
    array = [int(array[i]) for i in range(2*size)]
    print(solve(array, 2*size))
