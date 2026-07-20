class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            for i in range(len(grid)):
                for j in range(len(grid[0])-2, -1, -1):
                    grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]
            for i in range(len(grid)-2, -1, -1):
                grid[i][0], grid[i+1][0] = grid[i+1][0], grid[i][0]


        return grid