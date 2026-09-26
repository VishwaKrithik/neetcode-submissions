class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)

        def expand_from_center(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1        
            return l + 1, r
        
        maxL, maxR = 0, 0

        for center in range(n):
            l1, r1 = expand_from_center(center, center)
            l2, r2 = expand_from_center(center - 1, center)

            if r1 - l1 > maxR - maxL:
                maxR = r1
                maxL = l1
            if r2 - l2 > maxR - maxL:
                maxR = r2
                maxL = l2            

        return s[maxL:maxR]