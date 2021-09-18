class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        index = 0
        grid_to_graph = {}

        # Scan over the grid
        for i in range(m):
            for j in range(n):
                # If water ignore
                if grid[i][j] == "0":
                    continue
                # Else index grid to graph
                grid_to_graph[(i,j)] = index
                index += 1

        # Graph
        adjacent = [[] for _ in range(index)]

        # Scan over the grid
        # Create graph of connected land
        for i in range(m):
            for j in range(n):
                # If water ignore
                if grid[i][j] == "0":
                    continue
                # Connect neighbors
                neighbors = adjacent[grid_to_graph[(i,j)]]
                # If there is land to the left
                if j > 0 and grid[i][j-1] == "1":
                    neighbors.append(grid_to_graph[(i,j-1)])
                # If there is land to the right
                if j < n-1 and grid[i][j+1] == "1":
                    neighbors.append(grid_to_graph[(i,j+1)])
                # If there is land on top
                if i > 0 and grid[i-1][j] == "1":
                    neighbors.append(grid_to_graph[(i-1,j)])
                # If there is land on bottom
                if i < m-1 and grid[i+1][j] == "1":
                    neighbors.append(grid_to_graph[(i+1,j)])

        visited = [False for _ in range(index)]

        def explore(u):
            visited[u] = True
            for v in adjacent[u]:
                if visited[v] == False:
                    explore(v)

        count = 0
        for u in range(index):
            if not visited[u]:
                explore(u)
                count += 1

        return count