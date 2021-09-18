# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca = None

        def recursion(node):
            nonlocal LCA
            if node is None:
                return False

            left = recursion(node.left)
            right = recursion(node.right)
            parent = node.val == p.val or node.val == q.val

            if left+right+parent == 2:
                lca = node

            return left or parent or right

        recursion(root)
        return LCA