class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in seen:
                lng = 0
                while num in seen:
                    lng += 1
                    num += 1
                longest = max(lng, longest)

        return longest