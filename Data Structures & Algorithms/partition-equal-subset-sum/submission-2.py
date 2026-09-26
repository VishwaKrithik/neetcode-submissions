class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2: return False

        target = sum(nums) // 2

        bits = 1

        for num in nums:
            bits |= bits << num
            if (bits >> target) & 1:
                return True
        
        return (bits >> target) & 1 == 1