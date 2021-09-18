# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        max_length = 0

        def longest_path_length(root):
            """Length of the longest path ending in root"""
            nonlocal max_length

            # Base case
            if root is None:
                return 0

            # Compute the length longest path reaching left child
            left = longest_path_length(root.left)

            # Compute the length longest path reaching right child
            right = longest_path_length(root.right)

            # Add the missing vertices
            # If there are child to reach
            if root.left is not None:
                left += 1
            if root.right is not None:
                right += 1

            # Compute path length going throughout root
            length = left + right

            if max_length < length:
                max_length = length

            return max(left, right)

        longest_path_length(root)
        return max_length
