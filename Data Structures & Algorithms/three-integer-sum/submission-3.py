class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum1 = nums[i] + nums[j] + nums[k]

                if sum1 > 0:
                    k -= 1
                elif sum1 < 0:
                    j += 1
                else:
                    soln = [nums[i], nums[j], nums[k]]
                    res.append(soln)
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        
        return res

        # so edge cases 
        """res = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                sum1 = nums[i] + nums[j] + nums[k]

                if sum1 > 0:
                    k -= 1
                elif sum1 < 0:
                    j += 1
                else:
                    soln = [nums[i], nums[j], nums[k]]
                    if soln not in res:
                        res.append(soln)
                    j += 1
                    k -= 1
        
        return res"""
