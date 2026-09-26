class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [0] * len(nums)
        dp[0] = nums[0]

        if len(nums) == 1:
            return True

        if dp[0] == 0:
            return False

        for i in range(1, len(nums) - 1):
            dp[i] = max(dp[i - 1] - 1, nums[i])

            if dp[i] == 0:
                return False
        
        return True