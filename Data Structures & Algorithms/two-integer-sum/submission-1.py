class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, h in enumerate(nums):
            diff = target - h
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[h] = i
        return

        """for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]"""