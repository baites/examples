# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root, None

        # Temporal reference to root right side
        temp = root.right
        # Root right side is then flatten of left subtree
        root.right, last_node = self.flatten(root.left)
        if last_node is None:
            last_node = root
        # Set node right to be flatten if root right subtree
        last_node.right, node = self.flatten(temp)
        if node is not None:
            last_node = node
        # Set root left None
        root.left = None
        return root, last_node