# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        prev = slow.next = None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur


        while head and prev:
            head.next, head = prev, head.next
            head, prev = prev, head
        