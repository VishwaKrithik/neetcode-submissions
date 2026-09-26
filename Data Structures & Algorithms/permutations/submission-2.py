class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        seen = set()

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    path.append(num)
                    dfs(path)
                    seen.remove(num)
                    path.pop()
        
        dfs([])
        return res
                