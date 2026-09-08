class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            # Base Case: Out of bounds, hit water, or already mapped
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in visit):
                return 0

            # Mark current square as mapped
            visit.add((r,c))

            # Expand the search in all 4 directions
            down = dfs(r + 1, c)
            up = dfs(r - 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            # Return this square (1) plus all connected land
            return (1 + down + up + left + right)
        
        # Initiate the scan across the grid
        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area, dfs(r, c))
        
        return area

