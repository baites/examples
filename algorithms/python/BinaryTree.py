#! /usr/bin/env python2

from Queue import Queue

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:

    def __init__(self):
        self.root = None


    def printTree(self, order = 'preorder', root = None):
        if root:
            if order == 'preorder':
                print root.data
            if root.left:
                self.printTree(order, root.left)
            if order == 'inorder':
                print root.data
            if root.right:
                self.printTree(order, root.right)
            if order == 'postorder':
                print root.data
        else:
            self.printTree(order, self.root)


    def printBF(self, root = None):
        if root:
            S = set()
            Q = Queue()
            S.add(root.data)
            Q.put(root)
            while not Q.empty():
                node = Q.get()
                print node.data
                if node.left:
                    Q.put(node.left)
                if node.right:
                    Q.put(node.right)
                #if node.left and not node.left.data in S:
                #    S.add(node.left.data)
                #    Q.put(node.left)
                #if node.right and not node.right.data in S:
                #    S.add(node.right.data)
                #    Q.put(node.right)
        else:
            self.printBF(self.root)


    def insert(self, data, root = None):
        root = root if root else self.root
        if root:
            if data < root.data:
                if root.left:
                    self.insert(data, root.left)
                else:
                    root.left = BinaryTreeNode(data)
            else:
                if root.right:
                    self.insert(data, root.right)
                else:
                    root.right = BinaryTreeNode(data)
        else:
            self.root = BinaryTreeNode(data)


    def find(self, data, node = None, root = None):
        if node:
            if data < node.data:
                if node.left:
                    return self.find(data, node.left, node)
                else:
                    return None, None
            elif data > node.data:
                if node.right:
                    return self.find(data, node.right, node)
                else:
                    return None, None
            else:
                return node, root
        else:
            return self.find(data, self.root, None)


t = BinaryTree()

t.insert(3)
t.insert(6)
t.insert(5)
t.insert(2)
t.insert(10)
t.insert(9)
t.insert(13)

t.printTree()
print
t.printTree('inorder')
print
t.printTree('postorder')

node, root  = t.find(2)
print node.data, root.data

print
print 'BF'
t.printBF()

