# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        values = {}

        def check(node, level=0):
            if node is None:
                return
            values.setdefault(level, []).append(node.val)
            check(node.left, level+1)
            check(node.right, level+1)

        check(root)

        result = []

        for i in range(len(values)):
            if i%2 != 0:
                values[i].reverse()
            result.append(values[i])

        return result
