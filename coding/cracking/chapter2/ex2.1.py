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

values = [1, 2, 3, 3, 3, 4, 5, 5, 6, 6]

head = None

for value in reversed(values):
    head = push(head, value)
print_list(head)

def remove_dups(node):
    head = node
    prev_nodes = []
    prev_node = None
    counters = {}
    while node:
        value = node.value
        counters[value] = counters.get(value, 0) + 1
        if counters[value] > 1:
            prev_nodes.append(prev_node)
        prev_node = node
        node = node.next
    for prev_node in reversed(prev_nodes):
        node = prev_node.next
        if node:
            prev_node.next = node.next
            node.next = None
    return head

head = remove_dups(head)
print_list(head)
