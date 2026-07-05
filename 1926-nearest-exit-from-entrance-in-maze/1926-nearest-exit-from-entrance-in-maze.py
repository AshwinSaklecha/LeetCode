class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # apply normal bfs 
        dq = deque()
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        entry_i, entry_j = entrance
        dq.append((entry_i, entry_j, 0)) # i, j, steps
        visited[entry_i][entry_j] = True
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]
        while dq:
            print("i am here ")
            curr_i, curr_j, curr_steps = dq.popleft()
            if (curr_i == len(maze) - 1 or curr_j == len(maze[0]) - 1 or curr_i == 0 or curr_j == 0) and curr_steps != 0:
                return curr_steps 
            for direction in range(4):
                new_i = curr_i + x[direction]
                new_j = curr_j + y[direction]
                if new_i >= 0 and new_j >= 0 and new_i < len(maze) and new_j < len(maze[0]) and visited[new_i][new_j] == False and maze[new_i][new_j] != "+":
                    visited[new_i][new_j] = True
                    dq.append((new_i, new_j, curr_steps + 1))
        return -1