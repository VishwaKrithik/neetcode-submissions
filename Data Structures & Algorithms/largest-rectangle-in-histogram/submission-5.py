class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        maxArea = 0
        stack = []
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                idx = stack.pop()
                height = heights[idx]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, width * height)

            stack.append(i)

        return maxArea