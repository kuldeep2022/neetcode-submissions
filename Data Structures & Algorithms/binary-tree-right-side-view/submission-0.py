# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Will be solving using BFS
        if not root:
            return []

        q = deque([root])
        res = [root.val]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                isRightSide = True

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if isRightSide and q:
                
                res.append(q[-1].val)
        
        return(res)
                


        