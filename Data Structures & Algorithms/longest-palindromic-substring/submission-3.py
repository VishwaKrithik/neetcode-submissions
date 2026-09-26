class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        p = [0] * n
        c = 0
        r = 0

        max_len = 0
        best_center = 0

        for i in range(1, n - 1):
            i_mirror = 2 * c - i

            if r > i:
                p[i] = min(r - i, p[i_mirror])

            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            
            if i + p[i] > r:
                r = i + p[i]
                c = i
            
            if p[i] > max_len:
                max_len = p[i]
                best_center = i
            
        start = (best_center - max_len) // 2
        return s[start: start + max_len]