class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        half = sum(nums) // 2
        dp = 1 << 0

        for num in nums:
            dp |= dp << num
        
        return (dp & (1 << half)) != 0
        