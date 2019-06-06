# python3

from sys import stdin

# Vertex of a splay tree

class Vertex:
  def __init__(self, key, a, k):
    self.key = key
    self.sum = a
    self.a = a
    self.k = k
    self.left = None
    self.right = None
    self.parent = None


def printnode(node):
    if node is None:
        print('none')
        return
    print('key = {}, sum = {}, a = {}, k = {}'.format(
        node.key,
        node.sum,
        node.a,
        node.k
    ))


def inorder(node):
    if node == None:
        return
    inorder(node.left)
    printnode(node)
    inorder(node.right)


# Splay tree implementation


def update(v):
  if v == None:
    return
  v.sum = v.a + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else:
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  else:
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v
    last = v
    if v.key == key:
      break
    if v.key < key:
      v = v.right
    else:
      v = v.left
  root = splay(last)
  return (next, root)


def split(root, key):
  (result, root) = find(root, key)
  if result == None:
    return (root, None)
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)


def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

# Code that uses splay tree to solve the problem

root = None

def insert(key, a, k):
  global root
  (left, right) = split(root, key)
  new_vertex = None
  if right == None or right.key != key:
    new_vertex = Vertex(key, a, k)
  root = merge(merge(left, new_vertex), right)

def erase(x):
  global root
  (left, right) = split(root, x)
  if right == None or right.key != x:
    root = merge(left, right)
    return
  old_node = right
  middle = old_node.left
  if middle:
    middle.parent = None
  right = old_node.right
  if right:
    right.parent = None
  del old_node
  root = merge(left, right)

def search(x):
  global root
  result, root = find(root, x)
  if result == None or result.key != x:
      return False
  return True

def sum(fr, to):
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  val = middle.sum if middle else 0
  root = merge(left, merge(middle, right))
  return val


def add_value(i, x):
  global root
  node, root = find(root, i)
  node.a += x
  update(node)
  next, root = find(root, i+1)
  if next is not None and next.a < node.a + node.k:
    add_value(i+1, node.a + node.k - next.a)


# Main program

n = int(input().strip())
a = input().strip().split()
a = [int(a[i]) for i in range(n)]
k = input().strip().split()
k = [int(k[i]) for i in range(n-1)]
q = int(input().strip())

for i in range(n):
    vk = k[i] if i < n-1 else 0
    insert(i+1, a[i], vk)

inorder(root)

for i in range(q):
    line = input().split()
    if line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        result = sum(l, r)
        print(result)
    elif line[0] == '+':
        i = int(line[1])
        x = int(line[2])
        node, root = find(root, i)
        add_value(i, x)
        inorder(root)
    else:
        print('unknown ops')
