# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Node counter
        counter = 0

        def reverse(node):
            # Pointer initialization
            curr = node.next
            prev = node
            prev.next = None
            # Check if there is a curr
            while curr is not None:
                # Save curr next poiter
                n3xt = curr.next
                # Point curr next toward prev
                curr.next = prev
                # Update pointers
                prev = curr
                curr = n3xt
            # Point the head to prev
            node = prev
            return node

        def cut(step, node):
            prev = node
            curr = node.next
            step -= 1
            while step > 0 and curr is not None:
                prev = curr
                curr = curr.next
                step -= 1
            prev.next = None
            return node, curr

        def join(node1, node2):
            if node1 is None:
                return node2
            prev = None
            curr = node1
            while curr is not None:
                prev = curr
                curr = curr.next
            prev.next = node2
            return node1

        def size(node):
            counter = 0
            curr = node
            while curr is not None:
                curr = curr.next
                counter += 1
            return counter

        result = None
        curr = head
        length = size(head)
        while curr is not None:
            prev, curr = cut(k, curr)
            if length >= k:
                prev = reverse(prev)
            result = join(result, prev)
            length -= k
        return result