class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def dfs(i, path):
            if i == len(s):
                res.append(path.copy())
                return
            
            for idx in range(i, len(s)):
                curr_str = s[i:idx + 1]
                if curr_str == curr_str[::-1]:
                    path.append(curr_str)
                    dfs(idx + 1, path)
                    path.pop()
            
        dfs(0, [])
        return res
                