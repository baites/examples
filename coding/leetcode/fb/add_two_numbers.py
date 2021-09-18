# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Usual sum with carry
        c = 0
        prev = None
        while l1 is not None or l2 is not None:
            d1 = 0 if l1 is None else l1.val
            d2 =  0 if l2 is None else l2.val
            d = d1 + d2 + c
            Z = None
            if d > 9:
                D = ListNode(d%10)
                c = 1
            else:
                D = ListNode(d)
                c = 0
            D.next = prev
            prev = D
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # If carry is still one create
        # next digit with 1
        if c == 1:
            D = ListNode(1)
            D.next = prev

        # Reverse the list
        prev = None
        curr = D
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev