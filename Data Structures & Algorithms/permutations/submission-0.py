class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        self.n = len(nums)
        seen = set()

        def backtrack(path):
            if len(path) == self.n:
                res.append(path.copy())
                return
            
            for i in range(self.n):
                if nums[i] in seen:
                    continue
                
                seen.add(nums[i])
                path.append(nums[i])
                backtrack(path)
                path.pop()
                seen.remove(nums[i])
        
        backtrack([])
        return res