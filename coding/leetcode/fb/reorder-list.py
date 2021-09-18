# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Search for the middle of the list
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # Now the slow pointer points to the middle of the list

        # Reversion string from middle pointer
        prev = None
        curr = slow
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # Now prev is the head of inverted half list

        # Merge the list one for each element
        first, second = head, prev
        while second.next is not None:
            tmp = first.next
            first.next = second
            first = tmp
            tmp = second.next
            second.next = first
            second = tmp
