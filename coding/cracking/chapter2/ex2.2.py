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

for value in range(10):
    head = push(head, value+1)
print_list(head)

def search_last_nth(forward, n):
    backward = forward
    prev = None

    while forward:
        backward = Node(forward.value)
        if prev:
            backward.next = prev
        prev = backward
        forward = forward.next

    counter = 1

    while backward and counter < n:
        backward = backward.next
        counter += 1

    return backward

node = search_last_nth(head, 4)
print(node.value)
