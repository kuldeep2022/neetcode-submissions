# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        I just learn to calculate the height of the tree by solving other question.
        The question which i solved is diameter of binary tree.
        I will try to use that logic in order to solve this problem.
        '''

        def dfs(root):
            if not root:
                return [True, 0]
            
            left,right = dfs(root.left), dfs(root.right)

            # calculate if tree is balance from left, right and root of tree
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1],right[1])]

        
        return dfs(root)[0]
        
        