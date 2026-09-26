class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            leng = r - l
            max_area = max(max_area, leng * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max_area = 0

        # l, r = 0, len(heights) - 1

        # while l < r:

        #     leng = r - l
        #     max_area = max(max_area, leng * min(heights[r], heights[l]))

        #     if heights[r] > heights[l]:
        #         l += 1
        #     else:
        #         r -= 1
        
        # return max_area
