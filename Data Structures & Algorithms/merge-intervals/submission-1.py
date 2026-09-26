class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        output = [intervals[0]]

        for start, stop in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], stop)
            else:
                output.append([start, stop])
        
        return output