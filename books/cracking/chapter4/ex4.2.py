

def connect(adj, a, b):
    stack = []
    visited = set()
    stack.append(a)
    visited.add(a)
    while len(stack) > 0:
        u = stack.pop()
        for v in adj[u]:
            if v in visited:
                continue
            if v == b:
                return True
            visited.add(v)
            stack.append(v)
    return False

import sys

data = [
    list(map(int, line.strip().split())) for line in sys.stdin.readlines()
]

a,b = data[0]
adj = data[1:]
print(adj, a, b)
print(connect(adj, a, b))
