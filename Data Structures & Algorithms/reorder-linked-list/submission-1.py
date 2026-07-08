# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return 
        slow = head
        fast = head
        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        mid.next = None

        cur = slow.next
        prev = slow
        prev.next = None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur


        while head and prev:
            head.next, head = prev, head.next
            head, prev = prev, head
        