class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def maxRob(start, stop):
            a, b = 0, 0

            for num in nums[start:stop]:
                a, b = b, max(a + num, b)
            
            return b
        

        return max(maxRob(0, len(nums) - 1), maxRob(1, len(nums)))