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


class DLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def btree_to_dllist(node):
    head = None
    tail = None

    def inorder(node):
        nonlocal head
        nonlocal tail
        if tail is None:
            tail = DLNode(node.key)
            head = tail
            return
        curr = DLNode(node.key)
        tail.next = curr
        curr.prev = tail
        tail = curr

    def explore(node):
        if node is None:
            return
        explore(node.left)
        inorder(node)
        explore(node.right)

    explore(node)
    if head == tail:
        return head
    tail.next = head
    head.prev = tail
    return head


def print_list(node):
    if node.prev is None or node.next is None:
        print('None <- {} -> None'.format(node.value))
        return
    print('{} <- {} -> {}'.format(
        node.prev.value, node.value, node.next.value
    ))
    head = node
    node = node.next
    while node != head:
        print('{} <- {} -> {}'.format(
            node.prev.value, node.value, node.next.value
        ))
        node = node.next

keys = [4,1,3,5,2,6,7]
tree = BSTree()
for key in keys:
    tree.insert(key)
dllist = btree_to_dllist(tree.root)
print_list(dllist)

# Output
# 7 <- 1 -> 2
# 1 <- 2 -> 3
# 2 <- 3 -> 4
# 3 <- 4 -> 5
# 4 <- 5 -> 6
# 5 <- 6 -> 7
# 6 <- 7 -> 1
