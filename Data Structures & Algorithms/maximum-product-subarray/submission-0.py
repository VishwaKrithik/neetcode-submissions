class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_prod = min_prod = answer = nums[0]

        for x in nums[1:]:
            old_max = max_prod
            old_min = min_prod

            max_prod = max(x, x * old_max, x * old_min)
            min_prod = min(x, x * old_max, x * old_min)

            answer = max(answer, max_prod)
        

        return answer