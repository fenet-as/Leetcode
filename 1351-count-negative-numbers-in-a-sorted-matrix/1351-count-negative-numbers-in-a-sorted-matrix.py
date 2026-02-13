class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        

        count = 0

        m = len(grid)
        n = len(grid[0])

        col = len(grid[0])
        for i in range(len(grid)):
            for j in range(col):
                if grid[i][j] < 0:
                    col = j
                    break
                count += 1
        return ((m*n)-count)


