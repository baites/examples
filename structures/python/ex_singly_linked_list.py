from pyds.SinglyLinkedList import SinglyLinkedList

slist = SinglyLinkedList()

values = [1, 2, 3, 4, 5]

print()
print('updating the front')
print()

for value in values:
    slist.push_front(value)

print(len(slist))

for value in range(2):
    print(slist.pop_front())

print(slist.front())
print(len(slist))

for value in slist:
    print(value)
