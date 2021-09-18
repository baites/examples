# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
   
        def popleft(root):
            # Placeholder for popped node
            popped = None

            # Recusive popleft
            # Is like delete without two child case
            def recursive_popleft(root):
                # Write access to popped
                nonlocal popped
                # Base case
                if root is None:
                    return root
                # Popleft for left node if possible
                if root.left is not None:
                    root.left = recursive_popleft(root.left)
                # If not possible root is either leaf or has one child
                else:
                    # Node with only left child
                    if root.left is None:
                        temp = root.right
                        popped = root
                        popped.left = None
                        popped.right = None
                        return temp
                    # Node with only right child
                    else:
                        temp = root.left
                        popped = root
                        popped.left = None
                        popped.right = None
                        return temp
                return root

            # Recursively popped the left most element.
            root = recursive_popleft(root)
            return root, popped

        root, prev_popped = popleft(root)
        init_popped = prev_popped

        while root is not None:
            root, popped = popleft(root)
            popped.left = prev_popped
            prev_popped.right = popped
            prev_popped = popped

        if prev_popped is not None:
            prev_popped.right = init_popped
            init_popped.left = prev_popped

        return init_popped
   