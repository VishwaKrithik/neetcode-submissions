class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
 
        while l < r:
            target_sum = nums[l] + nums[r]
            if target_sum == target:
                return [l + 1, r + 1]
            elif target_sum > target:
                r -= 1
            else:
                l += 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l, r = 0, len(nums) - 1

        # while l < r:
        #     sum1 = nums[l] + nums[r]
        #     if sum1 > target:
        #         r -= 1
        #     elif sum1 < target:
        #         l += 1
        #     else:
        #         return [l + 1, r + 1]
        # return []