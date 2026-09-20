class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direc = [[1, 0], [-1, 0], [0, 1], [0, 1]]
        row = len(grid)
        col = len(grid[0])
        area = 0
        visit = set()

        
        def dfs(r, c):
            
            if (r>=row or c>=col or c<0 or r<0 or grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r, c))
            return(1+ dfs(r+1, c) + dfs(r-1, c)+ dfs(r, c+1)+ dfs(r, c-1))

        for r in range(row):
            for c in range(col):
                area = max(area, dfs(r, c))
        return area
            