class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = ""

        for ch in s:
            if ch.isalnum():
                res += ch.lower()

        print(res)
        
        return res[::-1] == res