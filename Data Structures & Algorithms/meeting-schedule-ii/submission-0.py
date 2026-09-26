"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        intervals = [[interval.start, interval.end] for interval in intervals]
        
        intervals.sort()
        rooms = []

        for start, end in intervals:
            if rooms and start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)


        return len(rooms)