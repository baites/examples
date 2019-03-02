import copy

N = 5
S = list(range(1,N+1))

def get_subsets(index=0):
    if index == len(S):
        return [[]]
    subsets = get_subsets(index+1)
    subtmps = []
    for s in subsets:
        stmp = copy.copy(s)
        stmp.append(S[index])
        subtmps.append(stmp)
    return subsets + subtmps

print(S)
print(get_subsets())
