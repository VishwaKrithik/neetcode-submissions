class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        self.n = len(nums)
        nums.sort()

        def backtrack(start, value, path):
            if value == target:
                res.append(path.copy())
                return
            
            for i in range(start, self.n):
                if nums[i] + value > target:
                    return
                path.append(nums[i])
                backtrack(i, value + nums[i], path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
