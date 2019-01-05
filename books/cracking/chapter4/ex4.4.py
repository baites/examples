
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        node = self._head
        values = []
        while node != None:
            values.append(str(node.value))
            node = node.next
        return '->'.join(values)

    def push_back(self, value):
        node = LinkedListNode(value)
        if self._tail:
            self._tail.next = node
            self._tail = node
        else:
            self._tail = node
            self._head = node
        self._size += 1

    def pop_front(self):
        if not self._head:
            return None
        node = self._head
        self._head = node.next
        node.next = None
        if not self._head:
            self._tail = None
        self._size -= 1
        return node.value


def make_list(tree):
    L = LinkedList()
    Q = LinkedList()
    D = [-1]*len(tree)
    Q.push_back(0)
    D[0] = 0
    Dmax = 0
    nodes = []
    while len(Q) > 0:
        n = Q.pop_front()
        print(n)
        if D[n] > Dmax:
            L.push_back(nodes)
            nodes = [n]
            Dmax = D[n]
        else:
            nodes.append(n)
        l = 2*n+1
        r = 2*n+2
        if l < len(tree) and tree[l] and D[l] == -1:
            Q.push_back(l)
            D[l] = D[n] + 1
        if r < len(tree) and tree[r] and D[r] == -1:
            Q.push_back(r)
            D[r] = D[n] + 1
    L.push_back(nodes)
    return L

tree = ['d', 'b', 'f', 'a', 'c', 'e', None]
L = make_list(tree)

print(L)
