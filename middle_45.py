class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # First row: can only come from left
                if i == 0:
                    grid[i][j] += grid[i][j - 1]

                # First column: can only come from above
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]

                # Other cells: choose minimum of top and left
                else:
                    grid[i][j] += min(
                        grid[i - 1][j],
                        grid[i][j - 1]
                    )

        return grid[m - 1][n - 1]
