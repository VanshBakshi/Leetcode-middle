class Solution:
    def createGrid(self, m, n):
        grid = []

        for i in range(m):
            row = []
            for j in range(n):
                if i == 0 or j == n - 1:
                    row.append('.')
                else:
                    row.append('#')

            grid.append(''.join(row))

        return grid
