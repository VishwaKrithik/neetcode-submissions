class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = []
        soln = [0] * n

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                elt = stack.pop()
                soln[elt[1]] = idx - elt[1]
            stack.append([temp, idx])
        
        return soln