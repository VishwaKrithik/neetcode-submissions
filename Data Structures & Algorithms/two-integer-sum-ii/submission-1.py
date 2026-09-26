class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            sum1 = nums[l] + nums[r]
            if sum1 > target:
                r -= 1
            elif sum1 < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []