# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        check = deque()
        check.append([p,q])
        while check:
            l1, l2 = check.popleft()
            if l1 and l2 and l1.val == l2.val:
                    check.append([l1.left,l2.left])
                    check.append([l1.right,l2.right])
            elif l1 != l2:
                return False

        return True