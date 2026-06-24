class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))] 
        ans = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == False:
                    ans = ans or self.traverse(i, j, (-1, -1), visited, grid)
                    if ans :
                        return ans
        return ans
    def traverse(self, i, j, parent, visited, grid, ):
        visited[i][j] = True
        ans = False
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]
        for move in range(4):
            new_i = i + x[move]
            new_j = j + y[move]
            if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]):
                if visited[new_i][new_j] == False and grid[new_i][new_j] == grid[i][j]:
                    ans = ans or self.traverse(new_i, new_j, (i, j), visited, grid)
                elif visited[new_i][new_j] == True and grid[new_i][new_j] == grid[i][j] and (new_i != parent[0] and new_j != parent[1]):
                    return True
        return ans