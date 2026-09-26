class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        S = ""

        for i in s:
            if i.isalnum():
                S += i.lower()
        
        return S == S[::-1]