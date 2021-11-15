class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        cache = {}

        def get_word_neighbor(word):
            neighbors = []
            for neighbor in wordList:
                if neighbor in cache:
                    neighbors.append(neighbor)
                    continue
                diff = 0
                for index in range(len(word)):
                    diff += int(neighbor[index] != word[index])
                if diff == 1:
                    neighbors.append(neighbor)
                    cache.setdefault(neighbor, []).append(word)
            return neighbors


        def bfs():
            queue = deque((beginWord,))
            dist = {beginWord: 1}
            while len(queue) > 0:
                # pop element from queue
                word = queue.pop()
                # explore all the neighbor words
                for neighbor in get_word_neighbor(word):
                    if neighbor not in dist:
                        # push neighbor to the end of the queue
                        queue.appendleft(neighbor)
                        # compute neighbor distance
                        dist[neighbor] = dist[word] + 1
            return dist

        dist = bfs()

        return dist[endWord] if endWord in dist else 0