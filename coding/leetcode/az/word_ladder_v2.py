class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        size = len(beginWord)

        neighbors = defaultdict(list)
        for word in wordList:
            for index in range(size):
                neighbors[word[:index] + '*' + word[index+1:]].append(word)

        def bfs():
            queue = deque((beginWord,))
            dist = {beginWord: 1}
            while len(queue) > 0:
                # pop element from queue
                word = queue.pop()
                for index in range(size):
                    template = word[:index] + '*' + word[index+1:]
                    # explore all the neighbor words
                    for neighbor in neighbors[template]:
                        if neighbor == word:
                            continue
                        if neighbor not in dist:
                            # push neighbor to the end of the queue
                            queue.appendleft(neighbor)
                            # compute neighbor distance
                            dist[neighbor] = dist[word] + 1
            return dist

        dist = bfs()

        return dist[endWord] if endWord in dist else 0