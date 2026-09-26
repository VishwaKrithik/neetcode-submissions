class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # DP

        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]
            
            if j < n:
                res[i] = j - i
        
        return res



        # Stack

        """n = len(temperatures)
        stack = []
        soln = [0] * n

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                elt = stack.pop()
                soln[elt[1]] = idx - elt[1]
            stack.append([temp, idx])
        
        return soln"""