class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        x = sum(nums)

        return n * (n + 1) // 2 - x



        # ans = len(nums)

        # for i in range(len(nums)):
        #     ans ^= i ^ nums[i]
        
        # return ans