class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)

        maxHeap = [-cnt for cnt in counts.values()]

        heapq.heapify(maxHeap)

        cooldown_queue = deque()
        time = 0
        
        while maxHeap or cooldown_queue:
            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count != 0:
                    cooldown_queue.append((count, time + n))
            

            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(maxHeap, cooldown_queue.popleft()[0])
        
        return time
