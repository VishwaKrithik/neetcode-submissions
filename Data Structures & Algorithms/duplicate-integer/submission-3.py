class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Round 2 bitch
        seenNums = set()

        for num in nums:
            if num in seenNums:
                return True
            seenNums.add(num)

        return False



















        # Round 1
        """
        a = set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False
        """
        #return len(nums) != len(set(nums))