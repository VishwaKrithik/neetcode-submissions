import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        heap = []

        for num in set(nums):
            heapq.heappush(heap, (-counter[num], num))
        
        res = []
        for _ in range(k):
            i, num = heapq.heappop(heap)
            res.append(num)

        return res