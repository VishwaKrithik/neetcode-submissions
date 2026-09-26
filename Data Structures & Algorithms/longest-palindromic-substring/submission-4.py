class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""


        t = "@#" + "#".join(s) + "#$"

        n = len(t)
        p = [0] * n
        c, r = 0, 0

        center = 0

        for i in range(1, n - 1):
            i_mirror = 2 * c - i

            if r > i:
                p[i] = min(r - i, p[i_mirror])
            
            while t[i - 1 - p[i]] == t[i + 1 + p[i]]:
                p[i] += 1
            
            if i + p[i] > r:
                r = i + p[i]
                c = i
            
            if p[i] > p[center]:
                center = i
        
        
        length = p[center]
        start = (center - length) // 2

        return s[start: start + length]
            
