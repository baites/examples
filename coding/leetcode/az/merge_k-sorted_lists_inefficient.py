# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(list1, list2):
            # End of the recursion
            if list1 is None:
                return list2
            if list2 is None:
                return list1

            if list1.next == None:
                node = list2

            # Check value list 1 is larger
            if list1.val > list2.val:
                list2.next = merge(list1, list2.next)
                return list2

            # Else
            list1.next = merge(list1.next, list2)
            return list1

        size = len(lists)

        if size == 0:
            return None

        result = lists[size-1]
        size -= 1

        while size > 0:
            result = merge(result, lists[size-1])
            size -= 1
        return result
