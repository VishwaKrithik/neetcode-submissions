class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
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
        
        return res
