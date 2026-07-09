# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if not root:
            return res
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    res += ",N"
                else:
                    res = res + "," + str(node.val)
                    q.append(node.left)
                    q.append(node.right)
        return res[1:]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        l = data.split(",")
        root = TreeNode(int(l[0]))
        q = deque([root])
        idx = 1
        while q:
            cur = q.popleft()
            if l[idx] != "N":
                cur.left = TreeNode(int(l[idx]))
                q.append(cur.left)
            idx += 1
            if l[idx] != "N":
                cur.right = TreeNode(int(l[idx]))
                q.append(cur.right)
            idx += 1

        return root