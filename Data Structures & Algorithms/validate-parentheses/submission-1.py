class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dick = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in dick:
                if stack and dick[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0


















        # stack = []
        # closeToOpen = {")": "(", "}": "{", "]": "["}


        # if len(s) == 0:
        #     return True
        # if len(s) % 2 == 1:
        #     return False

        # for i in s:
        #     if i in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[i]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(i)
        
        # return True if not stack else False
            