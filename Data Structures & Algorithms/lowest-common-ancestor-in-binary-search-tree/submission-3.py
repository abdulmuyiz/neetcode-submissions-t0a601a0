# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getAncestor(self, root: TreeNode, check: TreeNode) -> List[TreeNode]:
        l = [root]

        while check.val != root.val:
            if check.val > root.val:
                root = root.right
            else:
                root = root.left
            l.append(root)

        return l

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l1 = self.getAncestor(root, p)
        l2 = self.getAncestor(root, q)

        lca = root
        index = 1
        while index < len(l1) and index < len(l2):
            if l1[index].val == l2[index].val:
                lca = l1[index]
            index += 1

        return lca