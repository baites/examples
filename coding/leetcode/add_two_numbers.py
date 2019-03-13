# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, A, B):
        """
        :type A: ListNode
        :type B: ListNode
        :rtype: ListNode
        """
        c = 0
        prev = None
        while A or B:
            a = A.val if A else 0
            b = B.val if B else 0
            z = a + b + c
            Z = None
            if z > 9:
                Z = ListNode(z%10)
                c = 1
            else:
                Z = ListNode(z)
                c = 0
            Z.next = prev
            prev = Z
            A = A.next if A else None
            B = B.next if B else None

        if c == 1:
            Z = ListNode(1)
            Z.next = prev

        R = None
        prev = None
        while Z:
            R = ListNode(Z.val)
            if prev:
                R.next = prev
            prev = R
            Z = Z.next

        return R


def push(head, value):
    temp = head
    head = ListNode(value)
    head.next = temp
    return head

def print_list(node):
    s = ''
    while node:
        if node.next:
            s += '{} -> '.format(node.val)
        else:
            s += '{}'.format(node.val)
        node = node.next
    print(s)

A = None
for value in [3,4,2]:
    A = push(A, value)
print_list(A)

B = None
for value in [4,6,5]:
    B = push(B, value)
print_list(B)

node = Solution().addTwoNumbers(A,B)
print_list(node)

# Runtime: 76 ms, faster than 53.87% of Python online submissions for Add Two Numbers.
# Memory Usage: 11 MB, less than 6.32% of Python online submissions for Add Two Numbers.
