class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # O(m * n) space basic binary search
        data = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                data.append(matrix[row][col])
        
        l, r = 0, len(data) - 1

        while l <= r:
            mid = (l + r) // 2
            if data[mid] == target:
                return True
            elif data[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
