class Solution:
    def countIslands(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    stack = [(i, j)]
                    total = 0

                    while stack:
                        x, y = stack.pop()

                        if grid[x][y] == 0:
                            continue

                        total += grid[x][y]
                        grid[x][y] = 0

                        if x > 0 and grid[x - 1][y] > 0:
                            stack.append((x - 1, y))

                        if x + 1 < m and grid[x + 1][y] > 0:
                            stack.append((x + 1, y))

                        if y > 0 and grid[x][y - 1] > 0:
                            stack.append((x, y - 1))

                        if y + 1 < n and grid[x][y + 1] > 0:
                            stack.append((x, y + 1))

                    if total % k == 0:
                        count += 1

        return count
