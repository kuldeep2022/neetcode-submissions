# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        cnt = k
        def inOrder(root):
            nonlocal cnt,res
            if not root:
                return
            inOrder(root.left)
            cnt -= 1
            if cnt == 0:
                res = root.val
                return 
            inOrder(root.right)
        inOrder(root)
        
        return res

        