class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        self.n = len(nums)
        nums.sort()

        def dfs(start, val, path):
            if val == target:
                res.append(path.copy())
                return
            
            for i in range(start, self.n):
                if nums[i] + val > target:
                    break
                
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                dfs(i + 1, val + nums[i], path)
                path.pop()
        
        dfs(0, 0, [])
        return res
