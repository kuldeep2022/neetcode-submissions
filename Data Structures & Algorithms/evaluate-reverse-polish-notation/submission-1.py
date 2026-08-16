class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))

            else:
                v2,v1 = stack.pop(),stack.pop()
                if t == "+":
                    res = v1 + v2
                    stack.append(res)
                elif t == "-":
                    res = v1 - v2
                    stack.append(res)
                elif t == '*':
                    res = v1 * v2
                    stack.append(res)
                else:
                    res = int(v1 / v2)
                    stack.append(res)
        
        print(stack)
        return stack[0]

        