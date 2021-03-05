# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l = self.mergeTwoLists(l1.next, l2.next)

        start = l
        prev = None
        
        while l is not None and l.val < l1.val:
            prev = l
            l = l.next
        if prev is None:
            l1.next = l
            start = l1
        elif l is None:
            prev.next = l1
        else:
            prev.next = l1
            l1.next = l

        prev = None
        l = start
            
        while l is not None and l.val < l2.val:
            prev = l
            l = l.next
        if prev is None:
            l2.next = l
            start = l2
        elif l is None:
            prev.next = l2
        else:
            prev.next = l2
            l2.next = l
            
        return start
