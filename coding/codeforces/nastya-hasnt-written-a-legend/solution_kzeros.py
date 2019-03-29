# python3

from pyds.AVLBinarySearchTree import AVLBinarySearchTreeNode
from pyds.AVLBinarySearchTree import AVLBinarySearchTree
from pyds.IntervalTree import Interval, IntervalTreeNode
from pyds.IntervalTree import IntervalTree
from sys import stdin


class EInterval(Interval):
    """Implement an enhanced interval."""
    def __init__(self, low, high, a):
        super().__init__(low, high)
        self.a = a
        self.asum = a


# Define base class node using AVL policy
NodeBase = IntervalTreeNode(
    nodetype=AVLBinarySearchTreeNode
)

class Node(NodeBase):
    """Implement the tree node class."""

    def __init__(self, low, high, a):
        super().__init__(
            EInterval(low, high, a)
        )

    def label(self):
        """Customize node label."""
        return '[{},{}]|{},{}'.format(
            self.key.low, self.key.high, self.key.a, self.key.asum
        )

    def update(self):
        """Customize node update the keysum."""
        # Call parent update first
        super().update()
        self.maxhigh = self.key.high
        self.key.asum = self.key.a * (self.key.high-self.key.low+1)
        if self.left is not None:
            left = self.left
            self.maxhigh = max(self.maxhigh, left.maxhigh)
            self.key.asum += left.key.asum
        if self.right is not None:
            right = self.right
            self.maxhigh = max(self.maxhigh, right.maxhigh)
            self.key.asum += right.key.asum


# Define base class tree using AVL policy
TreeBase = IntervalTree(
    treetype=AVLBinarySearchTree
)

class Tree(TreeBase):
    """Implement the tree node class."""

    def __init__(self, root=None):
        """Constructor."""
        super().__init__(root)

    def interval(self, point):
        """Reimplement interval just to point a point."""
        return super().interval(
            Interval(point, point)
        )

    def end_interval(self, a):
        """Search last interval to be updated."""
        node = self._root
        while 1:
            if a > node.key.a:
                if node.right is None:
                    break
                node = node.right
            elif a < node.key.a:
                if node.left is None:
                    break
                node = node.left
            else:
                break
        if a < node.key.a:
            return node.prev()
        return node


def CreateTree(a):
    """Create a tree of intervals."""
    # Initially all the intervals are size 1
    n = len(a)
    tree = Tree()
    for i in range(len(a)):
        tree.insert(Node(i+1, i+1, a[i]))
    return tree


def Sum(ltree, i, j):
    """Compute the sum between elements based on intervals."""

    # Search for interal where index i is present O(log N)
    start = ltree.interval(i);
    # Search for interal where index j is present O(log N)
    end = ltree.interval(j);

    # Case if start and end intervals are the same
    if start.key.low == end.key.low:
        return start.key.a * (j-i+1)

    # Case if start and end are different
    # Split the tree in three section
    if start.key.low == 1:
        mtree = ltree
    else:
        mtree = ltree.split(start.key)
    rtree = mtree.split(end.key)

    # The middle tree contains all the intervals
    # from the next-to-start until end interval
    # So the root of the middle tree has the sum
    # except for contribution from start node.
    asum = mtree._root.key.asum

    # Rebuild the tree
    mtree.merge(rtree)
    if start.key.low == 1:
        return asum - start.key.a * (i-start.key.low)\
                    - end.key.a * (end.key.high-j)
    # Merge left side
    ltree.merge(mtree)
    # Return the sum after adding start and
    # end interval fractional contribution
    return asum + start.key.a * (start.key.high-i+1)\
                - end.key.a * (end.key.high-j)


def Add(tree, i, x):
    """Add a value and recompute intervals if needed."""

    # Edge case
    if x == 0:
        return

    # Search interval overlaping with index i O(log N)
    start = tree.interval(i)

    # Compute the new value of a
    a = start.key.a + x

    # Search end interval to update O(log N)
    end = tree.end_interval(a)

    # There is one node O(log N)
    if start.key == end.key:
        node = tree.delete(start.key)
        # Interval has one one point
        if node.key.low == node.key.high:
            node.key.a = a
            tree.insert(node)
            return
        # Interval has multiple points
        if i > node.key.low:
            tree.insert(
                Node(node.key.low, i-1, node.key.a)
            )
        tree.insert(Node(i, node.key.high, a))
        return

    # Remove all the intervals in the middle
    # by splitting the tree O(?)
    mtree = tree.split(start.key)
    node = tree.delete(start.key)
    rtree = mtree.split(end.key)

    # Insert needed nodes in the left tree
    if i > node.key.low:
        tree.insert(
            Node(node.key.low, i-1, node.key.a)
        )
    tree.insert(
        Node(i, end.key.high, a)
    )
    # Merge the right tree discarding the middle
    tree.merge(rtree)


def main():

    n = int(input().strip())
    a = input().strip().split()
    a = [int(a[i]) for i in range(n)]
    #k = input().strip().split()
    #k = [int(k[i]) for i in range(n-1)]
    q = int(input().strip())

    tree = CreateTree(a)

    for j in range(q):
        #print(j, tree)
        #print()
        line = input().split()
        if line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            print(Sum(tree, l, r))
        elif line[0] == '+':
            i = int(line[1])
            x = int(line[2])
            #print('+ {} {}'.format(i, x))
            Add(tree, i, x)
        else:
            print('unknown ops')

    #print(tree)

if __name__ == "__main__":
    main()
