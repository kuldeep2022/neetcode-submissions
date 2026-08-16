# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Can be easliy solved with DFS using recursio.
        '''
        if not root:
            return
        
        def preOrder(node):
            if not node:
                return
            
            node.left,node.right = node.right,node.left
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
      
        return root

        