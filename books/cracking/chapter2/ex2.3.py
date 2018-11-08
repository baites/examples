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

head = None
node = None

for value in range(1,10):
    head = push(head, value)
    if value == 4: node = head
print_list(head)

def remove_node(node):
    last = None
    while node.next:
        node.value = node.next.value
        last = node
        node = node.next
    if last:
        last.next = None

node = remove_node(node)
print_list(head)
