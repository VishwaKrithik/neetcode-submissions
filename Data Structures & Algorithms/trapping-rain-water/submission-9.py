class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        area = 0

        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        right[-1] = height[-1]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        area = 0

        for i in range(1, n - 1):
            h = min(left[i], right[i])

            area += h - height[i]
        
        return area

        # for center in range(1, n - 1):
            
        #     leftMax = 0
        #     for left in range(0, center):
        #         leftMax = max(leftMax, height[left])

        #     rightMax = 0
        #     for right in range(center + 1, n):
        #         rightMax = max(rightMax, height[right])
            
            
        #     h = min(leftMax, rightMax)
        #     area += max(h - height[center], 0)
            
        # return area