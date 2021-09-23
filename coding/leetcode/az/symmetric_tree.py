# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def preorder_left_first(node, nodes):
            """Visit tree preorder left first"""
            if node is None:
                nodes.append(1000)
                return
            nodes.append(node.val)
            preorder_left_first(node.left, nodes)
            preorder_left_first(node.right, nodes)

        def preorder_right_first(node, nodes):
            """Visit tree preorder right first"""
            if node is None:
                nodes.append(1000)
                return
            nodes.append(node.val)
            preorder_right_first(node.right, nodes)
            preorder_right_first(node.left, nodes)

        left_nodes = []
        preorder_left_first(root.left, left_nodes)

        right_nodes = []
        preorder_right_first(root.right, right_nodes)

        return left_nodes == right_nodes