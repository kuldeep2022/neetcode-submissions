# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #DFS
        def dfs(node,maxval):
            if not node:
                return 0
            
            res = 1 if node.val>= maxval else 0
            maxval = max(maxval,node.val)
            res += dfs(node.left,maxval)
            res += dfs(node.right,maxval)
            return res
        
        return dfs(root,root.val)

        #BFS
        # res = 0
        # q = deque()
        # q.append((root,-float('inf')))

        # while q:
        #     node,maxval = q.popleft()
        #     if node.val >= maxval:
        #         res+=1
            
        #     if node.left:
        #         q.append((node.left,max(maxval,node.val)))
            
        #     if node.right:
        #         q.append((node.right,max(maxval,node.val)))
        # return res
        