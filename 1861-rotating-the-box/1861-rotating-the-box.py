class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
        for i in range(len(grid)):
            for j in range(len(grid[i]) - 1, -1, -1):
                if grid[i][j] == "#":
                    last_empty_spot = -1
                    for k in range(j+1, len(grid[i])):
                        if grid[i][k] == "#" or grid[i][k] == "*":
                            break
                        last_empty_spot = k
                    if last_empty_spot != -1: #then we can swap
                        grid[i][j], grid[i][last_empty_spot] = grid[i][last_empty_spot], grid[i][j]
        new_box = [[] for _ in range(len(grid[0]))]
        for j in range(len(grid[0])):
            for i in range(len(grid) - 1, -1, -1):
                new_box[j].append(grid[i][j])
        return new_box