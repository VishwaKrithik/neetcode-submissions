class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(path, target, start):
            if target == 0:
                res.append(path.copy())
                return

            for idx in range(start, len(nums)):
                if target - nums[idx] < 0:
                    continue
                path.append(nums[idx])
                dfs(path, target - nums[idx], idx)
                path.pop()
        
        dfs([], target, 0)
        return res
