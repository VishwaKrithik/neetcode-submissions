class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calculate_distance(x, y):
            return math.sqrt(x**2 + y**2)
        
        heap = []

        for x, y in points:
            heap.append([calculate_distance(x, y), x, y])
        
        heapq.heapify(heap)
        ans = []
        while k > 0:
            k -= 1
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])
        
        return ans