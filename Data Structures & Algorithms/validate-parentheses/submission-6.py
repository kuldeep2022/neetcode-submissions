class Solution:
    def isValid(self, s: str) -> bool:
        '''
        The goal is every opening bracket should have a matchiing closing bracket.
        '''

        hMap = {'}':'{',")":"(","]":"["}
        stack = []

        for i,v in enumerate(s):
            if v in hMap:
                if not stack or hMap[v] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(v)
        return True if not stack else False

            
            

            
        