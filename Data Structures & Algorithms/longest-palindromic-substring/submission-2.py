class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checker(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                right += 1
                left -= 1
            
            return right - left - 1, right - 1, left + 1
        
        max_p = 0
        max_left = 0
        max_right = 0

        for c in range(len(s)):
            p1, r1, l1 = checker(c, c)
            p2, r2, l2 = checker(c - 1, c)

            if p1 > max_p:
                max_p = p1
                max_right = r1
                max_left = l1
            if p2 > max_p:
                max_p = p2
                max_right = r2
                max_left = l2
        
        return s[max_left:max_right + 1]