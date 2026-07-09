# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.d = {val: idx for idx, val in enumerate(inorder)}
        
        self.idx = 0
        def dfs(l, r):
            if l > r:
                return
            root = TreeNode(preorder[self.idx])
            mid  = self.d[preorder[self.idx]]
            self.idx +=1
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root


        return dfs(0,len(inorder) - 1)

