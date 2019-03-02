
def print_matrix(m):
    size = len(m)
    for i in range(size):
        print(' '.join(map(lambda x: str(x), m[i])))


def set_zeros(m):
    M = len(m)
    N = len(m[0])
    column = [False]*M
    row = [False]*N

    for i in range(M):
        for j in range(N):
            if m[i][j] == 0:
                column[i] = True
                row[j] = True

    for i in range(M):
        for j in range(N):
            if column[i] or row[j]:
                m[i][j] = 0

    return m


m = [
[1, 1, 1, 2],
[4, 1, 0, 2],
[4, 0, 1, 2],
[6, 3, 3, 1]
]
print_matrix(m)
print()
n = set_zeros(m)
print_matrix(n)
print('\n')
