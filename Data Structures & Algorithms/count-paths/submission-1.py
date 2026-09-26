class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if n == 1 or m == 1:
            return 1

        rows = m
        cols = n

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(1, rows):
            dp[r][0] = 1
        
        for c in range(1, cols):
            dp[0][c] = 1

        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        return dp[-1][-1]