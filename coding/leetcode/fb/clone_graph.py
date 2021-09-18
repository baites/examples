from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        # Visited set
        visited = {}

        # Place the first node
        queue = deque([node])
        visited[node.val] = Node(node.val)

        # Loop over the queue until is empty
        while len(queue) > 0:
            # Pop the node
            n = queue.pop()
            # Loop over the neighbors
            for neighbor in n.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val, [])
                    queue.appendleft(neighbor)
                visited[n.val].neighbors.append(visited[neighbor.val])

        return visited[node.val]
