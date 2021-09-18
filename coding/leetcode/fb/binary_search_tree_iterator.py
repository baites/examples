import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        # placeholder for parents
        self._parents = []
        # points to the initial root of the tree
        self._root = root
        # points to last node return by next
        self._last = None
        # cache for next value (when calling hasNext)
        #self._next = None

    def _left_most(self, root):
        node = root
        while node.left is not None:
            self._parents.append(node)
            node = node.left
        return node

    def next(self) -> int:
        # Initialization
        if self._last is None:
            self._last = self._left_most(self._root)
            return self._last.val

        # If right pointer is not None
        if self._last.right is not None:
            # Add last as parent
            self._parents.append(self._last)
            # Search the left most node
            self._last = self._left_most(self._last.right)
            return self._last.val

        # Define node as last
        node = self._last
        # If no right pointer, the
        # next (if exist) must be the parent
        # with a no None right pointer
        self._last = None
        # Loop over the list of parents
        while len(self._parents) > 0:
            # Pop a parent for the bread crumb list
            parent = self._parents.pop()
            # Chech if has a not None right
            if parent.right is not None and parent.right.val != node.val:
                self._last = parent
                break
            # Point node to the parent and iterate
            node = parent
        return None if self._last is None else self._last.val

    def hasNext(self) -> bool:
        """Implement as a next call but saving the state
        previous to the call."""
        # Saving state
        parents = copy.copy(self._parents)
        last = self._last
        # Main query
        result = self.next() is not None
        # Recovering the state
        self._parents = parents
        self._last = last
        return result

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()