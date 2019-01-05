import copy

N = 4
S = list(range(1,N+1))

def get_subsets():
    size = 2**len(S)
    subsets = []
    for i in range(0,size):
        bitmap = i
        index = 0
        subset = []
        while index < len(S):
            if bitmap & 1:
                subset.append(S[index])
            bitmap = bitmap >> 1
            index += 1
        subsets.append(subset)
    return subsets

print(S)
print(get_subsets())
