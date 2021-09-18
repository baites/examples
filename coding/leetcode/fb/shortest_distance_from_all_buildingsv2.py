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
        def get_bulding_distance(f, distance):
            # Create a queue for BFS
            queue = deque([f])
            # Distance of a bulding to itself is zero
            distance[f][f] = 0
            # BFS to measure distance
            while len(queue) > 0:
                # Pop index to a node
                u = queue.pop()
                # Look at the neightbors
                for v in adjacent[u]:
                    # If neightbor not visit when
                    # explorign from bulding f
                    if distance[f][v] == -1:
                        # Add neightbor to queue
                        queue.appendleft(v)
                        # Compute distance from
                        # bulding f to neightbor v
                        distance[f][v] = distance[f][u] + 1
                        # v is a bulding
                        if v in distance:
                            # Get distance from building f to v
                            distance_f_to_v = distance[f][v]
                            # Loop over all the distance computed
                            # from bulding f
                            for s in range(len(distance[f])):
                                # Ingnore unreachable/unkown points
                                if distance[f][s] == -1:
                                    continue
                                # The distance from bulding from v to s is
                                # the distance from f to v minus
                                # the distance from f to s
                                distance[v][s] = distance_f_to_v - distance[f][s]


        # The vailable distance is a dictionary
        # from a building v to any other node (lot or obstacle)
        #
        # BFS to compute distances from building f to all the nodes
        #   distance[f][] = [0, 1, -1, -1, 2, ..., 4, ...]
        #                       ^ node s           ^ is a building v
        # Implicitly you know a lot of distances from v
        #   distance[v][] = [4, 3, -1, -1, 2, ..., 0, ...]
        #                       ^ distance[v][s] = dist[f][v] - dist[f][v]
        #                                        = 4 - 1 = 3
        # This is because if distance[f][s] is known for some index s
        # when computing the distance from f then
        #
        # distance[v][s] = distance[f][v] - distance[f][s]
        #
        # Build a DFS that update for both the computed and implicit
        # distance from buildings

        # Measure from buildings
        # to any point other obstacles
        distance = {
            building: [-1]*len(adjacent) for building in buildings
        }
        for building in buildings:
            get_bulding_distance(building, distance)

        # Placeholder for max distance
        min_dist = -1

        # Scand the lots
        for lot in lots:
            dist = 0
            # Compute the sum of the distance to all buildings
            for building in buildings:
                temp = distance[building][lot]
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