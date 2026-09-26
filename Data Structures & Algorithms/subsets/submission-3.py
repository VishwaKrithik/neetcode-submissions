class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(path, start):
            res.append(path.copy())

            for idx in range(start, len(nums)):
                path.append(nums[idx])
                dfs(path, idx + 1)
                path.pop()
        
        dfs([], 0)
        return res