# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return dummy.next