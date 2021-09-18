# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        old_to_new = {}

        def listcopy(old):
            if old is None:
                return None
            new = Node(old.val)
            old_to_new[id(old)] = new
            new.next = listcopy(old.next)
            return new

        def randomcopy(old):
            if old is None:
                return
            new = old_to_new[id(old)]
            if old.random is not None:
                new.random = old_to_new[id(old.random)]
            randomcopy(old.next)

        new = listcopy(head)
        randomcopy(head)
        return new