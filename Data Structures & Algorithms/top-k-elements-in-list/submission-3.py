class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        nums.sort(key = lambda x: freq[x], reverse = True)

        seen = set()
        new_nums = []

        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            new_nums.append(num)

        nums = new_nums

        return nums[:k]