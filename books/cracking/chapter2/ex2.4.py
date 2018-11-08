class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def push(head, value):
    temp = head
    head = Node(value)
    head.next = temp
    return head

def print_list(node):
    s = ''
    while node:
        if node.next:
            s += '{} -> '.format(node.value)
        else:
            s += '{}'.format(node.value)
        node = node.next
    print(s)

a = [5,1,3]
b = [2,9,7]
A = None
for value in [5,1,3]:
    A = push(A, value)
print_list(A)

B = None
for value in [2,9,5,5]:
    B = push(B, value)
print_list(B)

def sum_lists(A,B):
    c = 0
    prev = None
    while A or B:
        a = A.value if A else 0
        b = B.value if B else 0
        z = a + b + c
        Z = None
        if z > 9:
            Z = Node(z%10)
            c = 1
        else:
            Z = Node(z)
            c = 0
        Z.next = prev
        prev = Z
        A = A.next if A else None
        B = B.next if B else None

    R = None
    prev = None
    while Z:
        R = Node(Z.value)
        if prev:
            R.next = prev
        prev = R
        Z = Z.next

    return R

node = sum_lists(A,B)
print_list(node)
