class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # check for no rows
        rows = len(grid)
        cols = len(grid[0])

        distance_map = [[0] * cols for _ in range(rows)]
        houses = [[0] * cols for _ in range(rows)]
        def neighbors(q, r, c, d):
            q.append((r - 1, c, d + 1))
            q.append((r, c - 1, d + 1))
            q.append((r, c + 1, d + 1))
            q.append((r + 1, c, d + 1))

        def bfs(r, c):
            visited = [[0] * cols for _ in range(rows)]
            q = deque()
            neighbors(q, r, c, 0)
            while q:
                r, c, d = q.popleft()
                if 0 <= r < rows and 0 <= c < cols and not visited[r][c] and grid[r][c] == 0:
                    visited[r][c] = 1
                    neighbors(q, r, c, d)
                    distance_map[r][c] += d
                    houses[r][c] += 1

        num_houses = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_houses += 1
                    bfs(r, c)

        mindist = math.inf
        for r in range(rows):
            for c in range(cols):
                if houses[r][c] == num_houses:
                    mindist = min(mindist, distance_map[r][c])
        if mindist == math.inf:
            return -1
        return mindist


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