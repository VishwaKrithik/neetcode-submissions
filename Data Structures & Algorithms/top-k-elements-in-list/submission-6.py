import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        maxHeap = []

        for num, val in counter.items():
            maxHeap.append([-val, num])
        
        heapq.heapify(maxHeap)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        
        return res