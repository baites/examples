
class BTNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTree:

    def __init__(self):
        self.root = None

    @staticmethod
    def _find(key, node):
        if node.key == key:
            return key
        elif node.key > key:
            if node.left is not None:
                return BSTree._find(key, node.left)
            return node
        else:
            if node.right is not None:
                return BSTree._find(key, node.right)
            return node

    def find(self, key):
        if self.root is None:
            raise IndexError('find from empty tree')
        return self._find(key, self.root)

    def insert(self, key):
        if self.root is None:
            self.root = BTNode(key)
            return
        node = self.find(key)
        if node.key > key:
            node.left = BTNode(key)
        elif node.key < key:
            node.right = BTNode(key)

    @staticmethod
    def _rexplore(node, preorder, inorder, postorder):
        if node is None:
            return
        if preorder is not None:
            preorder(node)
        BSTree._rexplore(node.left,
            preorder, inorder, postorder
        )
        if inorder is not None:
            inorder(node)
        BSTree._rexplore(node.right,
            preorder, inorder, postorder
        )
        if postorder is not None:
            postorder(node)

    def rexplore(self,
        preorder=None, inorder=None, postorder=None
    ):
        if self.root is None:
            return
        BSTree._rexplore(self.root,
            preorder, inorder, postorder
        )

    @staticmethod
    def _iexplore(node, preorder, inorder, postorder):
        stack = [(False, False, node)]
        while len(stack) > 0:
            expleft, expright, node = stack.pop()
            if not expleft:
                if preorder is not None and not expright:
                    preorder(node)
                if node.left is not None:
                    stack.append((True, expright, node))
                    stack.append((False, False, node.left))
                    continue
            if not expright:
                if inorder is not None:
                    inorder(node)
                if node.right is not None:
                    stack.append((expleft, True, node))
                    stack.append((False, False, node.right))
                    continue
            if postorder is not None:
                postorder(node)

    def iexplore(self,
        preorder=None, inorder=None, postorder=None
    ):
        if self.root is None:
            return
        BSTree._iexplore(self.root,
            preorder, inorder, postorder
        )

def print_node(node):
    if node is None:
        print('null')
    print('key = {}'.format(node.key))

keys = [4,1,3,5,2,6,7]

tree = BSTree()

for key in keys:
    tree.insert(key)
tree.rexplore(postorder=print_node)
print()
tree.iexplore(postorder=print_node)
