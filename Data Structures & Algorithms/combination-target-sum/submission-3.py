class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        self.n = len(nums)

        def backtrack(start, value, path):
            if value == target:
                res.append(path.copy())
                return
            
            if value > target or start >= len(nums):
                return
            
            path.append(nums[start])
            backtrack(start, value + nums[start], path)
            path.pop()
            backtrack(start + 1, value, path)
        
        backtrack(0, 0, [])
        return res
