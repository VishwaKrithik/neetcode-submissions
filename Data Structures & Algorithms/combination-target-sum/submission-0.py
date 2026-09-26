class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        self.n = len(nums)

        def backtrack(start, value, path):
            if value == target:
                res.append(path.copy())
                return
            
            if value > target:
                return
            
            for i in range(start, self.n):
                path.append(nums[i])
                backtrack(i, value + nums[i], path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
