from collections import deque

def bfs(adj, u):
    dist = [-1]*len(adj)
    prev = [None]*len(adj)
    thenode = u
    dist[u] = 0
    queue = deque()
    queue.appendleft(u)
    while len(queue) > 0:
        u = queue.pop()
        for v in adj[u]:
            if dist[v] == -1 or dist[v] == 0:
                dist[v] = dist[u] + 1
                prev[v] = u
                if v == thenode:
                    return dist[v], prev
                queue.appendleft(v)
    return -1, []

def print_cycle(path, u):
    v = path[u]
    result = str(u)
    while v != u:
        result += ' <- {}'.format(v)
        v = path[v]
    result += ' <- {}'.format(v)
    print(result)

def find_shortest_cycle(adj, u):
    dist, path = bfs(adj, u)
    if dist != -1:
        print('cycle size:', dist)
        print_cycle(path, u)
    else:
        print('no cycle')

adj = [
[1],
[2,3],
[4,5,6],
[0],
[],
[],
[0]
]

find_shortest_cycle(adj, 0) # return 0 <- 3 <- 1 <- 0
find_shortest_cycle(adj, 1) # return 0 <- 3 <- 1 <- 0
find_shortest_cycle(adj, 3) # return 0 <- 3 <- 1 <- 0
find_shortest_cycle(adj, 2) # return 2 <- 1 <- 0 <- 6 <- 2
find_shortest_cycle(adj, 6) # return 6 <- 2 <- 1 <- 0 <- 6
find_shortest_cycle(adj, 4) # return "no cycle"
