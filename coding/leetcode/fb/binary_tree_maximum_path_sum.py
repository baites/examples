# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        max_length = None

        def get_max_path(root):
            nonlocal max_length

            left_length = 0
            if root.left is not None:
                left_length = get_max_path(root.left)
            right_length = 0
            if root.right is not None:
                right_length = get_max_path(root.right)
            root_lengths = {
                left_length + right_length + root.val: max(left_length, right_length) + root.val,
                left_length + root.val: left_length + root.val,
                right_length + root.val: right_length + root.val,
                root.val: root.val
            }
            root_max_length = max(root_lengths.keys())
            max_length = root_max_length if max_length is None else max(max_length, root_max_length)
            return root_lengths[root_max_length]

        get_max_path(root)
        return max_length
