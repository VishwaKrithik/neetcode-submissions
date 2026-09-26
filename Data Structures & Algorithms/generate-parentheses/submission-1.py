class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(path, openB, closeB):
            if openB == closeB == n:
                res.append("".join(path))
                return
            
            if openB < n:
                path.append("(")
                dfs(path, openB + 1, closeB)
                path.pop()
            
            if closeB < openB:
                path.append(")")
                dfs(path, openB, closeB + 1)
                path.pop()

        dfs([], 0, 0)
        return res