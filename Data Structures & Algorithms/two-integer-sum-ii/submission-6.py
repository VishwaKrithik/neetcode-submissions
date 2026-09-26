class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = nums[left] + nums[right]

            if mid == target:
                return [left + 1, right + 1]
    
            if mid < target:
                left += 1
            else:
                right -= 1
        

        return [-1, -1]