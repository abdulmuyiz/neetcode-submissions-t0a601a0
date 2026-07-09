# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def compare(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if q and p and q.val == p.val:
            return (self.compare(p.left,q.left) and self.compare(p.right,q.right ))
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()
            if self.compare(node,subRoot):
                return True
            elif node != None:
                stack.append(node.left) 
                stack.append(node.right)


        return False