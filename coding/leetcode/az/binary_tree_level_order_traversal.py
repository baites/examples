from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        old_level = -1
        node_list = []
        queue = deque([(0, root)])
        while len(queue) > 0:
            level, node = queue.pop()
            if level != old_level:
                node_list.append([node.val])
            else:
                node_list[level].append(node.val)
            old_level = level
            if node.left is not None:
                queue.appendleft((level+1, node.left))
            if node.right is not None:
                queue.appendleft((level+1, node.right))
        return node_list
