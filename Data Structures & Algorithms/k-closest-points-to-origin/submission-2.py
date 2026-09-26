class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calculate_distance(x, y):
            return math.sqrt(x**2 + y**2)
        
        maxHeap = []
        for x, y in points:
            dist = -calculate_distance(x, y)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        
        return res
        
