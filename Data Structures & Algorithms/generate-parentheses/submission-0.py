class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        soln = []

        def dfs(count1, count2, s):
            if count1 == count2 and count1 == n:
                soln.append(s)
                return
            if count1 < n:
                dfs(count1 + 1, count2, s + "(")
            if count2 <  count1:
                dfs(count1, count2 + 1, s + ")")
        
        dfs(0, 0, "")

        return soln