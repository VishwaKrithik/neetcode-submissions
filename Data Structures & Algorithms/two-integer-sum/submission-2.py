class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Round 2 bitch
        prevNums = {}

        for idx, num in enumerate(nums):
            req = target - num
            if req in prevNums:
                return [prevNums[req], idx]
            prevNums[num] = idx
        
        return []











        
        


        # prevMap = {}

        # for i, h in enumerate(nums):
        #     diff = target - h
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[h] = i
        # return

        """for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]"""