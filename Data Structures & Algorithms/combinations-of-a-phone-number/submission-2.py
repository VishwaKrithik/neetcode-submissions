class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits or digits == "":
            return []

        res = []
        dtc = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(path, start):
            if start == len(digits):
                res.append("".join(path))
                return
            
            for char in dtc[digits[start]]:
                path.append(char)
                dfs(path, start + 1)
                path.pop()
        

        dfs([], 0)
        return res
