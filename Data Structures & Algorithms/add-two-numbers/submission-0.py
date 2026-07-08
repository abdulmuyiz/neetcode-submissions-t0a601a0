# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        carry_over = 0
        res = ListNode()
        output = res
        while first or second:
            if first and second:
                add = first.val + second.val + carry_over
                first = first.next
                second = second.next
            elif first:
                add =  first.val + carry_over
                first = first.next
            elif second:
                add = second.val + carry_over   
                second = second.next      
            carry_over = add // 10
            res.next = ListNode( add % 10  )
            res = res.next

        if carry_over:
            res.next = ListNode( carry_over )

        return output.next