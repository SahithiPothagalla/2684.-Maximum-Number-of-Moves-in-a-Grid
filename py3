class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [True] * n
        for c in range(1, m):
            new_dp = [False] * n
            for r in range(n):
                new_dp[r] |= (grid[r][c - 1] < grid[r][c]) and dp[r]
                if r > 0:
                    new_dp[r] |= (grid[r - 1][c - 1] < grid[r][c]) and dp[r - 1]
                if r < n - 1:
                    new_dp[r] |= (grid[r + 1][c - 1] < grid[r][c]) and dp[r + 1]
            if not any(new_dp):
                return c - 1
            dp = new_dp
        return m - 1
