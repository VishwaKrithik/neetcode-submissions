class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return bin(n).count('1')

        count = 0

        for _ in range(32):
            count += n & 1
            n >>= 1
        
        return count