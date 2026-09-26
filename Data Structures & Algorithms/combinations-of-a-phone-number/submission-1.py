class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        numToDigit = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in numToDigit[digit]:
                    tmp.append(curStr + c)
            res = tmp
        
        return res



        # res = []

        # def dfs(i, path):
        #     if i == len(digits):
        #         res.append(path)
        #         return
            
        #     for char in numToDigit[digits[i]]:
        #         dfs(i + 1, path + char)
        
        # dfs(0, "")
        # return res