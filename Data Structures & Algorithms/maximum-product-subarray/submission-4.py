class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxP, minP = 1, 1 
        g_max = nums[0]

        for num in nums:
            temp = maxP * num
            maxP = max(maxP * num, num, minP * num)
            minP = min(minP * num, temp, num)
            g_max = max(maxP, g_max)
        
        return g_max