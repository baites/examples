# Definition for a binary data node.
class dataNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a data to a single string.

        :type root: dataNode
        :rtype: str
        """

        # Placeholder for data serialization
        data = deque()

        # Base case
        if root is None:
            return data

        # Create a queue for BFS
        queue = deque([root])

        # Implement BFS
        while len(queue) > 0:
            # Pop a value from queue
            node = queue.pop()
            # The the node value accounting for Nones
            value = None if node is None else node.val
            # Add value to data list
            data.appendleft(value)
            # If node is node no check for childs
            if node is None:
                continue
            # Append neighbor nodes
            queue.appendleft(node.left)
            queue.appendleft(node.right)

        return data


    def deserialize(self, data):
        """Decodes your encoded data to data.

        :type data: str
        :rtype: dataNode
        """

        node = None

        while len(data) > 0:
            value = data.pop()
            # Get the value
            leftnode = TreeNode(value)


        return recursion(0)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))