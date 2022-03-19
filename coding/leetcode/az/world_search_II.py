class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Index to matched char in word
        m = len(board)
        n = len(board[0])

        # Result place holder
        results = []

        def search(i, j, trie):
            """Recursive search.
               i,j: indexes in the grid
            """
            nonlocal m, n


            # Read current char
            char = board[i][j]
            # Get next trie node
            node = trie[char]

            # If matched word add to result
            if '$' in node:
                # Pop matched words to avoid duplication
                results.append(node.pop('$'))

            # Mark board position a visited
            board[i][j] = '#'

            # Initialize neighbor found
            found = False

            # Search on the neighborhood
            if i > 0 and board[i-1][j] != '#' and board[i-1][j] in node:
                found = search(i-1, j, node)
            if not found and i < m - 1 and board[i+1][j] != '#' and board[i+1][j] in node:
                found = search(i+1, j, node)
            if not found and j > 0 and board[i][j-1] != '#' and board[i][j-1] in node:
                found = search(i, j-1, node)
            if not found and j < n - 1 and board[i][j+1] != '#' and board[i][j+1] in node:
                found = search(i, j+1, node)

            # Unset board visited
            board[i][j] = char

            # Remove all prefix trace to matched word
            # When word is matched node dict is empty
            if len(node) == 0:
                trie.pop(char)

        # Implement trie
        trie = {}

        # Loop over each word
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['$'] = word

        # Loop over the grid
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    search(i, j, trie)

        return results