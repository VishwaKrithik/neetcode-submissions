class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = []
        for i in nums:
            maxHeap.append(-i)
        
        heapq.heapify(maxHeap)
        while k > 1:
            k -= 1
            heapq.heappop(maxHeap)
        
        return -maxHeap[0]