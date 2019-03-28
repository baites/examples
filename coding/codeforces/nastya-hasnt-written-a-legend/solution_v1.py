# python3

from pyds.AVLBinarySearchTree import AVLBinarySearchTreeNode
from pyds.AVLBinarySearchTree import AVLBinarySearchTree
from sys import stdin


class Node(AVLBinarySearchTreeNode):
    """Implement avl node for implementing an interval tree."""

    def __init__(self, key, high, a):
        super().__init__(key)
        self.high = high
        self.maxhigh = high
        self.a = a
        self.asum = a

    def label(self):
        """Customize node label."""
        return '[{},{}]|{},{}'.format(self.key, self.high, self.a, self.asum)

    def update(self):
        """Customize node update the keysum."""
        # Call parent update first
        super().update()
        self.maxhigh = self.high
        self.asum = self.a * (self.high-self.key+1)
        if self.left is not None:
            left = self.left
            self.maxhigh = max(self.maxhigh, left.maxhigh)
            self.asum += left.asum + left.a * (left.high-left.key)
        if self.right is not None:
            right = self.right
            self.maxhigh = max(self.maxhigh, right.maxhigh)
            self.asum += right.asum + right.a * (right.high-right.key)

    def overlap(self, point):
        """Check if point overlaps with self."""
        if self.high < point or point < self.key:
            return False
        return True


class IntervalTree(AVLBinarySearchTree):
    """Implement interval tree based on AVL."""

    def __init__(self, root=None):
        """Constructor."""
        super().__init__(root)

    def interval(self, point):
        """Return a node that overlap with point."""
        node = self._root
        while node is not None \
            and not node.overlap(point):
            if node.left is not None \
                and node.left.maxhigh >= point:
                node = node.left
            else:
                node = node.right
        return node

    def end_interval(self, a):
        """Search last interval to be updated."""
        node = self._root
        while 1:
            if a > node.a:
                if node.right is None:
                    break
                node = node.right
            elif a < node.a:
                if node.left is None:
                    break
                node = node.left
            else:
                break
        if a < node.a:
            return node.prev()
        return node


def CreateTree(a, k):
    """Create a tree of intervals."""
    # Initially all the intervals are size 1
    n = len(a)
    tree = IntervalTree()
    for i in range(len(a)):
        vk = k[i] if i < n-1 else 0
        tree.insert(Node(i+1, i+1, a[i]))
    return tree


def GetSum(ltree, i, j):
    """Compute the sum between elements based on intervals."""

    # Search for interal where index i is present O(log N)
    start = ltree.interval(i);
    # Search for interal where index j is present O(log N)
    end = ltree.interval(j);

    # Case if start and end intervals are the same
    if start.key == end.key:
        return start.a * (j-i+1)

    # Case if start and end are different
    # Split the tree in three section
    if start.key == 1:
        mtree = ltree
    else:
        mtree = ltree.split(start.key)
    rtree = mtree.split(end.key)

    # The middle tree contains all the intervals
    # from the next to start until end interval
    # So the root of the middle tree has the sum
    # except for contribution from start node.
    asum = mtree._root.asum

    # Rebuild the tree
    mtree.merge(rtree)
    if start.key != 1:
        ltree.merge(mtree)

    # Return the sum after adding start interval contribution
    return asum + start.a * (start.high-i+1)


def Add(tree, i, x):
    """Add a value and recompute intervals if needed."""

    # Edge case
    if x == 0:
        return

    # Search interval overlaping with index i O(log N)
    start = tree.interval(i)

    # Compute the new value of a
    a = start.a + x

    # Search end interval to update O(log N)
    end = tree.end_interval(a)

    # No need for propagate the update
    # if start and end intervals are the same O(log N)
    if start.key == end.key:
        node = tree.delete(i)
        node.a = a
        tree.insert(node)
        return

    # Remove all the intervals in the middle
    # by splitting the tree O(?)
    mtree = tree.split(start.key)
    tree.delete(start.key)
    rtree = mtree.split(end.key)

    # Create a new interval covering
    # all the updated values O(log N)
    node = Node(start.key, end.key, a)
    # Insert the node in the left tree
    tree.insert(node)
    # Merge the right tree discarding the middle
    tree.merge(rtree)


def main():

    n = int(input().strip())
    a = input().strip().split()
    a = [int(a[i]) for i in range(n)]
    k = input().strip().split()
    k = [int(k[i]) for i in range(n-1)]
    q = int(input().strip())

    tree = CreateTree(a, k)

    for i in range(q):
        print(tree)
        print()
        line = input().split()
        if line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            print(GetSum(tree, l, r))
        elif line[0] == '+':
            i = int(line[1])
            x = int(line[2])
            Add(tree, i, x)
        else:
            print('unknown ops')

    print(tree)

if __name__ == "__main__":
    main()
