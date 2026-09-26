class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sub = 0
        numSet = set(nums)

        for n in nums:
            if (n - 1) not in numSet:
                sub = 0
                while (sub + n) in numSet:
                    sub += 1
                max_sub = max(max_sub, sub)
        return max_sub

        
        # Sorting
        """lst = sorted(set(nums))
        if lst == []:
            return 0
        sub = 1
        max_sub = 1
        for i in range(1, len(lst)):
            if lst[i - 1] + 1 == lst[i]:
                sub += 1
            else:
                max_sub = max(max_sub, sub)
                sub = 1
        max_sub = max(max_sub, sub)
        return max_sub"""