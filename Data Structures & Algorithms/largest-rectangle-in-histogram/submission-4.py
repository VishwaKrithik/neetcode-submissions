class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        left = [0] * n
        right = [0] * n

        left[0] = -1
        right[-1] = n

        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left[p]
            left[i] = p
        
        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p
        
        maxArea = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = width * heights[i]
            maxArea = max(area, maxArea)
        
        return maxArea