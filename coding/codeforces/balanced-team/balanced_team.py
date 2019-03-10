# http://codeforces.com/problemset/problem/1133/C

import bisect

def solve(skill, size):
    skill.sort()
    i = 0; j = 1
    maxsize = 1
    while j < size:
        if skill[j] - skill[i] <= 5:
            maxsize = max(maxsize, j-i+1)
        else:
            i = bisect.bisect_left(skill, skill[j]-5, i ,j)
        j += 1
    return maxsize

if __name__ == "__main__":
    size = int(input().strip())
    array = input().strip().split()
    array = [int(array[i]) for i in range(size)]
    print(solve(array, size))
