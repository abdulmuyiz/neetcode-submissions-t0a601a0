class Solution:

	def goodNodes(self, root: TreeNode) -> int:
		self.res = 0
		m = float("-inf")

		def dfs(cur,m):
			if not cur:
				return None
			if m <= cur.val:
				m = cur.val
				self.res += 1
			dfs(cur.right,m)
			dfs(cur.left, m)

		dfs(root,m)
		return self.res
