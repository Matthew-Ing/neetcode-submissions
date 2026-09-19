class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        row = len(board)
        col = len(board[0])

        def dfs(r, c, i):
            # true condition
            if i == len(word):
                return True
            # false conditions
            if (r<0 or c<0 or r >= row or c>=col):
                return False
            if (word[i] != board[r][c] or board[r][c] == '#'):
                return False
            # check each of them

            board[r][c]= '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False

        # check each of the starting points