from collections import deque

class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:

        # Get the size of the grid
        m = len(grid)
        n = len(grid[0])

        # Create a graph where each node
        # is a square on the grid
        adjacent = [[] for _ in range(m*n)]

        # Helper
        def index(i,j):
            return i*n + j

        # Helper
        def coord(index):
            return index//n, index%n

        # Helper
        def manhattan(inx1, inx2):
            i1, j1 = coord(inx1)
            i2, j2 = coord(inx2)
            return abs(i1-i2) + abs(j1-j2)

        # Save all the buildings
        buildings = set()

        # Empty lots
        lots = set()

        # Connect the nodes
        for i in range(m):
            for j in range(n):
                # Obtacle cannot be reached
                if grid[i][j] == 2:
                    continue
                elif grid[i][j] == 1:
                    buildings.add(index(i,j))
                else:
                    lots.add(index(i,j))
                if i > 0 and grid[i-1][j] not in (1,2):
                    adjacent[index(i,j)].append(index(i-1,j))
                if i < m-1 and grid[i+1][j] not in (1,2):
                    adjacent[index(i,j)].append(index(i+1,j))
                if j > 0 and grid[i][j-1] not in (1,2):
                    adjacent[index(i,j)].append(index(i,j-1))
                if j < n-1 and grid[i][j+1] not in (1,2):
                    adjacent[index(i,j)].append(index(i,j+1))

        # Measure distance to any node
        # from starting node u
        def distance(u):

            # Set distance (-1 is disconnected)
            dist = [-1]*len(adjacent)
            # Set a visited flags
            visited = [False]*len(adjacent)

            # Create a queue for BFS
            queue = deque([u])
            dist[u] = 0

            # BFS to measure distance
            while len(queue) > 0:
                u = queue.pop()
                visited[u] = True
                for v in adjacent[u]:
                    if not visited[v]:
                        queue.appendleft(v)
                        dist[v] = dist[u] + 1

            return dist

        # Measure from buildings
        # to any point other obstacles
        distance_from_building = {}
        for building in buildings:
            distance_from_building[building] = distance(building)

        # Placeholder for max distance
        min_dist = -1

        # Scand the lots
        for lot in lots:
                dist = 0
                # Compute the sum of the distance to all buildings
                for building in buildings:
                    temp = distance_from_building[building][lot]
                    if temp == -1:
                        dist = -1
                        break
                    dist += temp
                # Update min distance
                # Do not update if cannot reach
                # one of the buildings
                if dist == -1:
                    continue

                if min_dist == -1:
                    min_dist = dist
                elif min_dist > dist:
                    min_dist = dist

               # min_dist = min(min_dist, dist) if min_dist != -1 else dist

        return min_dist


grid = [
    [2,2,2,2,0,2,2,0,0,0,2,0,0,0,0,0,0,0,0,0,2,2,0,1,0,0,0,0,0,2,2,2,0,0,0,0,0,2,2,2,0,2,0,0],
    [0,0,2,2,0,0,0,2,0,0,2,2,0,0,0,0,2,0,2,1,0,2,0,1,2,2,2,0,0,2,0,2,2,0,0,0,0,2,2,0,2,1,2,0],
    [1,0,0,0,0,2,2,0,0,2,0,0,1,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,0,0,1,0,0,2,0,2,2,2,0,2,0,2,2,0],
    [1,0,2,0,0,2,0,0,2,0,0,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0],
    [0,0,2,0,0,0,0,0,0,0,2,0,2,0,1,0,2,2,2,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,2,0,2,0,1,0,2,2,0,2],
    [2,0,0,0,0,2,0,0,2,2,2,2,0,0,2,2,2,0,0,0,0,2,0,0,0,0,2,0,2,0,2,0,1,2,0,2,2,0,0,0,2,0,0,2],
    [0,0,0,2,2,2,0,2,0,0,0,2,0,0,2,0,2,0,2,0,0,2,0,2,0,1,0,2,2,0,0,2,0,0,0,2,2,2,2,0,0,0,2,0],
    [2,0,0,2,0,2,2,2,2,0,0,2,2,0,2,0,0,0,1,2,0,2,2,0,2,0,2,1,2,0,1,0,2,1,2,0,0,0,0,0,0,0,2,2],
    [0,0,2,2,0,2,0,0,0,2,0,2,0,2,2,0,2,0,0,0,0,0,0,0,2,0,0,2,1,2,0,0,0,2,1,0,2,2,2,0,0,0,2,0],
    [2,0,0,0,0,2,0,0,2,2,2,2,0,2,0,0,2,0,0,0,0,2,0,0,0,0,0,2,1,0,0,2,2,2,1,2,2,0,0,0,0,0,2,2],
    [0,1,0,2,0,0,2,0,0,2,0,0,0,0,0,0,1,2,0,2,2,2,2,0,0,2,2,2,0,2,0,2,2,2,0,0,2,0,0,0,0,0,2,2],
    [0,2,0,0,0,2,0,2,2,2,0,0,1,2,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,2],
    [2,2,2,2,2,2,0,0,0,0,0,2,0,2,2,2,0,2,0,2,0,2,2,0,2,0,0,0,2,0,0,2,2,2,2,2,0,0,0,2,0,2,2,0],
    [0,0,2,0,2,2,0,0,0,0,0,0,2,2,0,2,0,2,2,0,0,0,0,0,2,2,1,0,0,1,2,0,2,0,0,0,0,2,0,2,0,2,0,0],
    [0,2,2,0,0,0,0,2,0,0,0,2,0,2,2,0,0,2,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2,0,2,0,0],
    [0,0,0,0,0,2,2,0,2,2,0,0,0,2,2,2,0,2,2,0,2,0,2,0,2,2,0,1,0,2,0,2,0,0,2,0,0,0,0,0,0,2,0,2],
    [2,2,0,2,0,0,1,2,0,1,0,2,0,0,2,0,1,2,1,2,2,0,2,0,0,0,0,2,2,2,0,2,0,2,0,2,0,0,0,0,0,0,0,2],
    [0,2,2,0,2,0,0,1,0,0,0,0,2,0,0,0,0,0,2,2,0,2,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0,0,2,2,0,2,2],
    [0,2,2,0,0,2,2,0,2,0,0,0,0,0,2,2,0,0,0,2,2,2,1,0,2,2,0,2,0,0,2,0,0,0,1,2,0,2,2,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,2,2,0,0,0,2,2,1,0,0,2,2,0,2,0,2,0,1,0,2,0,0,0,0,2,0,2],
    [0,0,2,2,0,0,2,0,2,0,2,2,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,2,0,0,2,0,2,0,0,0,0,0,0,0],
    [0,2,2,2,2,0,0,2,0,0,2,2,0,0,0,2,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,2],
    [2,2,2,0,0,2,0,0,0,0,0,2,0,0,2,2,0,0,2,0,2,0,0,0,2,0,2,2,0,0,0,2,2,0,0,2,0,0,2,0,2,2,0,2],
    [2,0,0,2,2,2,0,0,0,2,2,0,0,0,0,0,2,0,0,0,0,0,2,0,0,2,0,1,0,1,0,0,2,0,2,0,2,0,2,1,0,2,0,0],
    [2,0,0,2,2,0,0,0,0,0,2,0,0,0,2,2,2,0,0,2,0,0,2,0,0,2,2,2,2,2,2,0,0,0,2,0,0,2,2,1,0,0,0,2],
    [1,0,2,0,2,0,0,2,0,0,0,2,0,1,0,0,2,2,0,0,2,0,2,0,2,2,0,0,0,2,0,0,0,0,2,2,2,2,0,2,2,2,0,2],
    [0,0,0,0,2,2,2,0,0,1,0,2,2,2,0,0,0,1,2,0,0,0,2,0,0,0,0,0,2,0,2,0,0,0,0,0,2,0,0,1,0,0,0,2],
    [0,2,2,0,2,0,2,1,2,2,1,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,2,2,2,0,0,2,0,2,0,2,0,0,0,2,0,0,0,0],
    [0,2,2,0,2,2,0,2,2,0,0,0,1,2,2,0,0,2,0,0,2,2,2,0,2,2,2,0,2,0,0,0,2,2,0,0,0,0,2,2,0,2,2,2],
    [0,0,2,0,0,0,1,2,0,2,2,2,0,0,2,2,0,0,0,2,0,0,2,0,0,2,2,2,0,2,2,0,0,0,0,2,0,0,0,0,0,0,2,2]]

#grid = [
#    [1,1,1,1,1,0],
#    [0,0,0,0,0,1],
#    [0,1,1,0,0,1],
#    [1,0,0,1,0,1],
#    [1,0,1,0,0,1],
#    [1,0,0,0,0,1],
#    [0,1,1,1,1,0]
#]

print(Solution().shortestDistance(grid))