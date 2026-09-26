class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = sorted(set(nums))
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
        return max_sub
            
