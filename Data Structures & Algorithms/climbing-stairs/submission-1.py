class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1 or n == 0:
            return 1
        

        a, b = 1, 1

        for _ in range(n - 1):
            a, b = b, a + b
        
        return b