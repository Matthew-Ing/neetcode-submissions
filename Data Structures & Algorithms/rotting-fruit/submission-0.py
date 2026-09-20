class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        time = 0
        fresh = 0
        row = len(grid)
        col = len(grid[0])
        direc = [[1,0], [-1,0], [0,1],[0,-1]]

        # init the queue
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])

        # start with the bfs
        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direc:
                    rows, cols = dr + r, dc + c
                    if (rows in range(row) and cols in range(col) and grid[rows][cols] == 1):
                        grid[rows][cols] = 2
                        q.append((rows,cols))
                        fresh-=1
            time +=1
        return time if fresh == 0 else -1

