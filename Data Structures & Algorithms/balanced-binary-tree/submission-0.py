class Solution:

	def isBalanced(self, root: Optional[TreeNode]) -> bool:

		self.res = True
		
		def dfs(curr):
			if not curr:
				return 0
			right = dfs(curr.right)
			left = dfs(curr.left)

			if (abs(right - left) > 1):
				print(right, left)
				self.res = False

			return 1 + max(right,left)
		dfs(root)
		return self.res
