class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        min_dist = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        qu = deque()
        qu.append((grid[0][0], 0, 0))
        visited[0][0] = True
        x = [0, 0, -1, 1]
        y = [1, -1, 0, 0]
        while qu :
            weight, i, j = qu.popleft()
            for direction in range(4):
                new_i = i + x[direction]
                new_j = j + y[direction]
                if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]) and visited[new_i][new_j] != True :
                    visited[new_i][new_j] = True
                    if grid[new_i][new_j] == 1:
                        min_dist[new_i][new_j] = weight + 1
                        qu.append((weight + 1, new_i, new_j))
                    else:
                        min_dist[new_i][new_j] = weight
                        qu.appendleft((weight, new_i, new_j))
        i = len(grid) - 1
        j = len(grid[0]) - 1
        return min_dist[i][j] < health