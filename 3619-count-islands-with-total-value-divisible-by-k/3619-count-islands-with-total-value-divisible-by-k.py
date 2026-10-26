class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == False and grid[i][j] != 0 :
                    ans += self.traverse(i, j, grid, visited, k)
        return ans
    def traverse(self, i, j, grid, visited, k):
        x = [0, 0, -1, 1]
        y = [1, -1, 0, 0]
        visited[i][j] = True
        dq = deque()
        dq.append((i, j))
        sum = 0
        while dq :
            i, j = dq.popleft()
            sum += grid[i][j]
            for dir in range(4):
                new_i = i + x[dir]
                new_j = j + y[dir]
                if new_i >= 0 and new_j >= 0 and new_i < len(grid) and new_j < len(grid[0]) and visited[new_i][new_j] == False and grid[new_i][new_j] != 0 :
                    dq.append((new_i, new_j))
                    visited[new_i][new_j] = True
        return 1 if sum % k == 0 else 0