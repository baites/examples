from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # Using queue for deserialization
        data = deque()

        # Recursive pre-order coding the tree
        def code(node):
            # Base case
            if node is None:
                data.appendleft(None)
                return
            # Saving node data
            data.appendleft(node.val)
            # Recursive call
            code(node.left)
            code(node.right)
        # Code from the root
        code(root)
        return data


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # Recusive pre0order decoding
        def decode():
            # Pop from the queue
            value = data.pop()
            # If none just return none
            if value is None:
                return None
            # Create tree node
            node = TreeNode(value)
            # Recursively get the left and right childs
            node.left = decode()
            node.right = decode()
            return node

        return decode()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))