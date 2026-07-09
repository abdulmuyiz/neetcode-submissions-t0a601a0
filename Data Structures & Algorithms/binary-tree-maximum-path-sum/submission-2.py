class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = float("-inf")
        def dfs_max(curr):
            if not curr:
                return float("-inf")
            rm = dfs_max(curr.right)
            lm = dfs_max(curr.left)
            temp = max([curr.val,curr.val+lm, curr.val+rm] )
            self.m = max([self.m,temp,curr.val+rm+lm])
            curr.val = temp
            return curr.val
        dfs_max(root)
        return self.m
		  

