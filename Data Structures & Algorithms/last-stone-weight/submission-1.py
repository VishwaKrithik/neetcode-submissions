class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first == second:
                continue
            else:
                heapq.heappush(heap, first - second)
        

        return -heap[0] if len(heap) == 1 else 0
