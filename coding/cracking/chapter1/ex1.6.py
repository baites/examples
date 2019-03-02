
def print_matrix(m):
    size = len(m)
    for i in range(size):
        print(' '.join(map(lambda x: str(x), m[i])))


def rotate90(m):
    size = len(m)
    dim = size
    off = 0
    for l in range(size//2):
        for j in range(dim-1):
            tmpA = m[dim-1+off][j+off]
            m[dim-1+off][j+off] = m[j+off][off]
            tmpB = m[dim-1-j+off][dim-1+off]
            m[dim-1-j+off][dim-1+off] = tmpA
            tmpA = m[off][dim-1-j+off]
            m[off][dim-1-j+off] = tmpB
            m[j+off][off] = tmpA
        dim -= 2
        off += 1
    return m

m = [
[0, 2, 0],
[1, 0, 1],
[0, 2, 0]
]
print_matrix(m)
print()
n = rotate90(m)
print_matrix(n)
print('\n')

m = [
[0, 1, 1, 0],
[4, 1, 0, 2],
[4, 0, 1, 2],
[0, 3, 3, 0]
]
print_matrix(m)
print()
n = rotate90(m)
print_matrix(n)
print('\n')
