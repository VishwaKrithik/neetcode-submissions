class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = -1

                area = 1
                for dr, dc in directions:
                    area += dfs(r + dr, c + dc)
            
                return area
            else:
                return 0
        
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        
        return max_area
            
        
