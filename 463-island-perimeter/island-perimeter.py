class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        p = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:

                    if i == 0 or grid[i - 1][j] == 0:
                        p += 1     #Up
                    if i == row - 1 or grid[i + 1][j] == 0:
                        p += 1     #Down
                    if j == 0 or grid[i][j - 1] == 0:
                        p += 1     #Left
                    if j == col - 1 or grid[i][j + 1] == 0:
                        p += 1
        return p                               