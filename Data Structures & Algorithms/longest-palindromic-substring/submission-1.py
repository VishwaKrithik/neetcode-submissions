class Solution:
    def longestPalindrome(self, s: str) -> str:

        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        p = [0] * n

        center = right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            
            if i + p[i] > right:
                right = i + p[i]
                center = i
        

        max_len = max(p)
        center_idx = p.index(max_len)

        start = (center_idx - max_len) // 2

        return s[start : start + max_len]