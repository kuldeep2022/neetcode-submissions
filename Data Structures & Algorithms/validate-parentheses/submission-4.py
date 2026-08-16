class Solution:
    def isValid(self, s: str) -> bool:
        '''
        The goal is every opening bracket should have a matchiing closing bracket.
        '''

        h = {'}':'{',')':'(', ']':'['}

        stack = []
        for i in s:
            if i not in h:
                print(i)
                stack.append(i)

            else:
                if stack and h[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
            
        