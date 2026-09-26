class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 or n == 1:
            return 1
        
        if m < n:
            m, n = n, m

        res = 1

        for i, j in zip(range(m, m + n - 1), range(1, n)):
            res = (res * i) // j
        
        return res