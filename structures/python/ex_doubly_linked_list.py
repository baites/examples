from pyds.DoublyLinkedList import DoublyLinkedList

dlist = DoublyLinkedList()

values = [1, 2, 3, 4, 5]

print()
print('updating the front')
print()

for value in values:
    dlist.push_front(value)

print(len(dlist))

for value in range(2):
    print(dlist.pop_front())

print(dlist.front())
print(len(dlist))

for value in dlist:
    print(value)

for value in reversed(dlist):
    print(value)

print()
print('updating the back')
print()

dlist = DoublyLinkedList()

for value in values:
    dlist.push_back(value)

print(len(dlist))

for value in range(2):
    print(dlist.pop_back())

print(dlist.back())
print(len(dlist))

for value in dlist:
    print(value)

for value in reversed(dlist):
    print(value)
