class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(needOpen,needClose):
            if needOpen == needClose == n:
                res.append("".join(stack))
            
            if needOpen < n:
                stack.append("(")
                backtrack(needOpen+1,needClose)
                stack.pop()
            
            if needClose < needOpen:
                stack.append(")")
                backtrack(needOpen,needClose + 1)
                stack.pop()
        
        backtrack(0,0)
        return (res)
        