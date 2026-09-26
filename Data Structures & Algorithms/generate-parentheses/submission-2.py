class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(left, right, path):
            if left == right == n:
                res.append("".join(path))
                return
            
            if left < n:
                path.append("(")
                dfs(left + 1, right, path)
                path.pop()
            if right < left and right < n:
                path.append(")")
                dfs(left, right + 1, path)
                path.pop()
            
        dfs(0, 0, [])
        return res
                