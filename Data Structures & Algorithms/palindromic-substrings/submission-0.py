class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        palindromes = 0

        def expand_around_center(l, r):
            nonlocal palindromes
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                palindromes += 1
            
        


        for center in range(n):
            expand_around_center(center, center)
            if center > 0:
                expand_around_center(center - 1, center)
        

        return palindromes