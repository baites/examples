#! /usr/bin/env python
"""Run DoubleLinkedList excersise."""

class DoubleLinkedNode:
    """Implement a double linked node."""

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


    def __str__(self):
        prev = self.prev.key if self.prev != None else 'None'
        next = self.next.key if self.next != None else 'None'
        return '%s -> %s -> %s' % (prev, self.key, next)



class DoubleLinkedList:

    def __init__(self):
        self.head = None


    def __str__(self):
        node = self.head
        elements = ''
        while node != None:
            elements += '%s ' % node.key
            node = node.next
        return elements


    def find(self, key):
        node = self.head
        while node and node.key != key:
            node = node.next
        return node


    def insert(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        node.prev = None


    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        del node


L = DoubleLinkedList()

L.insert(DoubleLinkedNode(1))
L.insert(DoubleLinkedNode(2))
L.insert(DoubleLinkedNode(4))

print(L)

print(L.find(1))
print(L.find(2))
print(L.find(4))

L.delete(L.find(2))

print(L)

L.delete(L.find(1))

print(L)

L.delete(L.find(4))

print(L)
