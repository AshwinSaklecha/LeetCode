class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        man_dist = self.multi_source_bfs(grid)
        # print(man_dist)
        min_safe_val = 0
        max_safe_val = max(map(max, man_dist))
        ans = self.binary_search(min_safe_val, max_safe_val, man_dist)
        return ans
    def multi_source_bfs(self, grid):
        man_dist = [[-1] * len(grid[0]) for _ in range(len(grid))]
        qu = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    man_dist[i][j] = 0
                    qu.append((i, j))
        x = [0, 0, -1, 1]
        y = [1, -1, 0, 0]
        while qu:
            lenofqu = len(qu)
            for _ in range(lenofqu):
                i, j = qu.popleft()
                for direction in range(4):
                    new_i = i + x[direction]
                    new_j = j + y[direction]
                    if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]) and man_dist[new_i][new_j] == -1:
                        man_dist[new_i][new_j] = man_dist[i][j] + 1
                        qu.append((new_i, new_j))
        return man_dist
    def binary_search(self, min_val, max_val, man_dist):
        s = min_val 
        e = max_val 
        ans = float('-inf') # maximize the answer 
        while s <= e :
            mid = (s + e) // 2
            if self.check(mid, man_dist): # this mid has to be the least element in the path
                ans = max(ans, mid)
                s = mid + 1
            else:
                e = mid - 1
        return 0 if ans == float('-inf') else ans
    def check(self, val, man_dist):
        qu = deque()
        visited = [[False] * len(man_dist[0]) for _ in range(len(man_dist))]
        if man_dist[0][0] < val or man_dist[len(man_dist)-1][len(man_dist[0]) - 1] < val:
            return False 

        x = [0, 0, -1, 1]
        y = [1, -1, 0, 0]
        
        qu.append((0, 0))
        visited[0][0] = True

        while qu :
            lenofqu = len(qu)
            for _ in range(lenofqu):
                i, j = qu.popleft()
                if i == len(man_dist) - 1 and j == len(man_dist[0]) - 1:
                    return True
                for direction in range(4):
                    new_i = i + x[direction]
                    new_j = j + y[direction]
                    if new_i >= 0 and new_i < len(man_dist) and new_j >= 0 and new_j < len(man_dist[0]) and man_dist[new_i][new_j] >= val and visited[new_i][new_j] == False:
                        visited[new_i][new_j] = True
                        qu.append((new_i, new_j))
        return False