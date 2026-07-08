# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        while node and lists:
            index, node.next = min(enumerate(lists), key=lambda x: x[1] != None and x[1].val )
            node = node.next
            lists[index] = lists[index].next
            if lists[index] == None:
                lists.pop(index)



        return dummy.next