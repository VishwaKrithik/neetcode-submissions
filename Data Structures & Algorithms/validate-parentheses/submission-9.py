class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack and (stack[-1] == "(" and ch == ")" or \
                    stack[-1] == "[" and ch == "]" or \
                    stack[-1] == "{" and ch == "}"):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0