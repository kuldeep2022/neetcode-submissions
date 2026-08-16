# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        def dfs(root,depth):
            nonlocal maxdepth
            if not root:
                maxdepth = max(maxdepth,depth)
                return
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        
        dfs(root,0)
        return maxdepth
        if not root:
            return 0
        q = deque([root])
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            res+=1
        
        return res
            
        
        