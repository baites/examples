# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def _find(val, node):
        if node.val == val:
            return val
        elif node.val > val:
            if node.left is not None:
                return BSTree._find(val, node.left)
            return node
        else:
            if node.right is not None:
                return BSTree._find(val, node.right)
            return node

    def find(self, val):
        if self.root is None:
            raise IndexError('find from empty tree')
        return self._find(val, self.root)

    def insert(self, val):
        if self.root is None:
            self.root = BTNode(val)
            return
        node = self.find(val)
        if node.val > val:
            node.left = BTNode(val)
        elif node.val < val:
            node.right = BTNode(val)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def serialize(self, root, array):
        if root is None:
            return
        self.serialize(root.left, array)
        array.append(root.val)
        self.serialize(root.right, array)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        array = []
        self.serialize(root, array)
        if len(array) == 1:
            return False
        i = 0
        j = len(array) - 1
        twosum = array[i] + array[j]
        while twosum != k:
            if twosum < k:
                i += 1
            else:
                j -= 1
            if i == j:
                return False
            twosum = array[i] + array[j]
        return True

vals = [2,3,4,5,6,7]
tree = BSTree()
for val in vals:
    tree.insert(val)

s = Solution()
print(s.findTarget(tree.root, 9))
