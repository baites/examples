
class BinaryTree:

  def __init__(self, data):
    self.n = len(data)
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      self.key[i] = data[i][0]
      self.left[i] = data[i][1]
      self.right[i] = data[i][2]


def check_balance(tree):
    stack = []
    stack.append((0, 0))
    while len(stack) > 0:
        key, depth = stack.pop()
        if tree.left[key] > 0:
            if depth > 1:
                return False
            stack.append((tree.left[key], depth+1))
        if tree.right[key] > 0:
            if depth > 1:
                return False
            stack.append((tree.right[key], depth+1))
    return True

import sys

data = [
    list(map(int, line.strip().split())) for line in sys.stdin.readlines()
]
tree = BinaryTree(data)
print(check_balance(tree))
