import copy

def find_paths(N):

    paths = []

    def find_path_r(path, n, m):
        if n < N-1:
            tmp = copy.copy(path)
            tmp.append((n,m))
            find_path_r(tmp, n+1, m)
        if m < N-1:
            tmp = copy.copy(path)
            tmp.append((n,m))
            find_path_r(tmp, n, m+1)
        if n == N-1 and m == N-1:
            path.append((n,m))
            paths.append(path)

    find_path_r([], 0, 0)

    return paths

print(len(find_paths(4)))
