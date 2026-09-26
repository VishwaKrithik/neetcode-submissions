import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []

        for num, cnt in counter.items():
            buckets[cnt].append(num)
        

        for idx in range(len(buckets) -1, -1, -1):
            for elt in buckets[idx]:
                res.append(elt)
                if len(res) == k:
                    return res
        