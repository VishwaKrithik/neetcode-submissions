class Solution:
    def countSubstrings(self, s: str) -> int:

        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"

        total = 0
        n = len(t)
        p = [0] * n
        c, r = 0, 0

        for i in range(1, n - 1):
            i_mirror = 2 * c - i

            if r > i:
                p[i] = min(r - i, p[i_mirror])

            if r > i:
                p[i] = min(r - i, p[i_mirror])
            
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
                
            if i + p[i] > r:
                c = i
                r = i + p[i]
                
            total += (p[i] + 1) // 2
            
        return total