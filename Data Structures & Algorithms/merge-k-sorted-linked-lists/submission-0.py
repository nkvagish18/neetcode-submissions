# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
            while head:
                values.append(head.val)
                head =  head.next
        values.sort()
        dummy = ListNode(0)
        temp = dummy
        for value in values:
            temp.next = ListNode(value)
            temp = temp.next
        return dummy.next