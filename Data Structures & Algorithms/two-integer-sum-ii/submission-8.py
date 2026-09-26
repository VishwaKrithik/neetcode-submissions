class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = nums[left] + nums[right]

            if mid == target:
                return [left + 1, right + 1]
            
            if mid > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]