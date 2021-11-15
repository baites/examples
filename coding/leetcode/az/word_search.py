class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Index to matched char in word
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]

        def search(i, j, c=0):
            """Recursive search.
               i,j: indexes in the grid
            """
            nonlocal m, n

            if board[i][j] != word[c]:
                return False

            if c == len(word)-1:
                return True

            visited[i][j] = True

            found = False
            if i > 0 and not visited[i-1][j]:
                found = search(i-1, j, c+1)
            if not found and i < m - 1 and not visited[i+1][j]:
                found = search(i+1, j, c+1)
            if not found and j > 0 and not visited[i][j-1]:
                found = search(i, j-1, c+1)
            if not found and j < n - 1 and not visited[i][j+1]:
                found = search(i,j+1, c+1)

            visited[i][j] = False
            return found

        for i in range(m):
            for j in range(n):
                if search(i,j):
                    return True

        return False
