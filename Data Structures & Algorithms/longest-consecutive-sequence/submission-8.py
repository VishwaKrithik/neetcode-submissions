class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in seen:
                count = 0
                while num in seen:
                    count += 1
                    num += 1
                max_length = max(count, max_length)
        
        return max_length