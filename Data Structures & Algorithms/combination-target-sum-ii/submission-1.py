class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        def dfs(path, target, start):
            if target == 0:
                res.append(path.copy())
                return
            if start == len(nums):
                return 

            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue
                if target - nums[idx] < 0:
                    return
                path.append(nums[idx])
                dfs(path, target - nums[idx], idx + 1)
                path.pop()
        
        dfs([], target, 0)
        return res
