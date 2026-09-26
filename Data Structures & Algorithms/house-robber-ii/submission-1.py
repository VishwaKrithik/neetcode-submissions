class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]

        def robber(l, r):
            rob1 = rob2 = 0

            for i in range(l, r):
                rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
            
            return rob2
        

        return max(robber(1, n), robber(0, n - 1))