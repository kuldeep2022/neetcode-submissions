# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        def dfs(node,depth):
            nonlocal maxD
            if not node:
                maxD = max(maxD,depth)
                return depth
            
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        dfs(root,0)
        return maxD
            

        '''
        I think I can solve this using BFS as I am thinking that
        Depth can also be consider similar to levels so maybe I can try that
        Let's see :)
        '''
        
        if not root:
            return 0
        q = deque([root])
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                #print(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            res +=1
        
        #print("RES",res)
        return res

        