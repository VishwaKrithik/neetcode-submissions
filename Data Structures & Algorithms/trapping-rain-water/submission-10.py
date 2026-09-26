class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        area = 0

        stack = []

        for current in range(n):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break

                distance = current - stack[-1] - 1

                bounded_height = min(height[current], height[stack[-1]]) - height[top]

                area += distance * bounded_height

            stack.append(current)

        return area