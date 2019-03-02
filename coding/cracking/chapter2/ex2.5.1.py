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
    counter = 0
    while node and counter < 10:
        if node.next:
            s += '{} -> '.format(node.value)
        else:
            s += '{}'.format(node.value)
        node = node.next
        counter += 1
    print(s)

head = None
node = None

for value in range(1,6):
    head = push(head, value)
    if value == 1:
        node = head
    elif value == 3:
        node.next = head
print_list(head)

def find_cycle(node):
    node_set = set()
    while node:
        if id(node) in node_set:
            break
        node_set.add(id(node))
        node = node.next
    return node

node = find_cycle(head)
print(node.value)
