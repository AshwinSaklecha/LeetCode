class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        islands = 0
        for i in range(len(grid)):
            last_idx = len(grid[0]) - 1
            first_idx = 0
            if grid[i][first_idx] == 0 and visited[i][first_idx] == False:
                self.traverse(i, first_idx, grid, visited)
            if grid[i][last_idx] == 0 and visited[i][last_idx] == False:
                self.traverse(i, last_idx, grid, visited)
        for j in range(len(grid[0])):
            last_idx = len(grid) - 1
            first_idx = 0
            if grid[first_idx][j] == 0 and visited[first_idx][j] == False:
                self.traverse(first_idx, j, grid, visited)
            if grid[last_idx][j] == 0 and visited[last_idx][j] == False:
                self.traverse(last_idx, j, grid, visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and visited[i][j] == False:
                        self.traverse(i, j, grid, visited)
                        islands += 1
        return islands 
    def traverse(self, i, j, grid, visited):
        visited[i][j] = True
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]

        for dir in range(4):
            new_i = i + x[dir]
            new_j = j + y[dir]
            if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]) and visited[new_i][new_j] == False and grid[new_i][new_j] == 0 :
                self.traverse(new_i, new_j, grid, visited)
        return 69