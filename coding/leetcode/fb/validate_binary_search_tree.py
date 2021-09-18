# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def inorder_check(root, condition):
        if root is None:
            return True
        check = Solution.inorder_check(root.left, condition)
        if not check:
            return check
        check = condition(root.val)
        if not check:
            return check
        return Solution.inorder_check(root.right, condition)

    def isValidBST(self, root: TreeNode) -> bool:

        # Based case of isValidBST
        if root is None:
            return True

        # Check that all the left values are less than the one in root
        check = self.inorder_check(root.left, lambda val: val<root.val)
        if not check:
            return check

        # Check that all the right values are greater than the one in root
        check = self.inorder_check(root.right, lambda val: val>root.val)
        if not check:
            return check

        # Check if left tree is valid BST
        check = self.isValidBST(root.left)
        if not check:
            return check

        # Check if right tree is valid BST
        return self.isValidBST(root.right)
