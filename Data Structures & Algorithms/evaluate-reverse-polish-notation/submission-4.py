class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:
            if i in "+-/*":
                a = int(stack.pop())
                b = int(stack.pop())

                if i == "+":
                    stack.append(b + a)
                elif i == "-":
                    stack.append(b - a)
                elif i == "*":
                    stack.append(b * a)
                elif i == "/":
                    stack.append(b / a)
            else:
                stack.append(i)
        
        return int(stack[-1])
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack = []
        
        # for i in tokens:
        #     if i == "+":
        #         stack.append(stack.pop() + stack.pop())
        #     elif i == "-":
        #         stack.append(-stack.pop() + stack.pop())    
        #     elif i == "*":
        #         stack.append(stack.pop() * stack.pop())
        #     elif i == "/":
        #         b, a = stack.pop(), stack.pop()
        #         stack.append(int(a/ b))
        #     else:
        #         stack.append(int(i))
        # return stack[0]

                

        # division is a fuckin cunt
        """for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                a = stack.pop()
                b = stack.pop()
                s = "(" + b + i + a + ")"
                stack.append(s)
        
        return int(eval(stack[-1]))"""