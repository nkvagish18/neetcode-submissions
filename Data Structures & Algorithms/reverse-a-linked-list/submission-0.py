# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        values.reverse()
        dummy = ListNode(0)
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next