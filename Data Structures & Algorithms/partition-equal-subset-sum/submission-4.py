class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        half = sum(nums) // 2
        dp = [False] * (half + 1)
        dp[0] = True

        for num in nums:
            for j in range(half, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[-1]
        