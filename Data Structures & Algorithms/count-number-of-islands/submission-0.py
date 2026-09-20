class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(r, c):
            # check if out of bounds
            if (r<0 or c<0 or r>= row or c >=col or grid[r][c] == "0"):
                return True

            grid[r][c] = "0"
            for dr, dc in direc:
                dfs(r+dr, c+dc)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count+=1
        return count