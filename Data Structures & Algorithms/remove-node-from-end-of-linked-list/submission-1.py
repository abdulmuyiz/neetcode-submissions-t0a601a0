# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = head
        length = 0
        while count:
            length += 1
            count = count.next

        if length == n:
            return head.next
        if length <= 1:
            return head

        start = head
        pos = length - n - 1
        while pos > 0:
            pos -= 1
            start = start.next
        start.next = start.next.next
        
        return head
