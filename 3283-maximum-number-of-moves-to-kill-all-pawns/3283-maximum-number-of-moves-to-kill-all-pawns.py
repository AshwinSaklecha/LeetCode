class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        positions.append([kx, ky])
        min_steps = [{} for _ in range(len(positions))]
        corresponding_node = {}
        counter = 0
        for position in positions:
            corresponding_node[tuple(position)] = counter 
            counter += 1
        for i in range(len(positions) - 1):
            for j in range(i+1, len(positions)):
                # from i to j
                my_dict1 = min_steps[i]
                my_dict2 = min_steps[j]
                distance_found = self.helper(positions[i], positions[j])
                my_dict1[j] = distance_found
                my_dict2[i] = distance_found
        mask = 0
        print(min_steps)
        # min steps is made 
        # final step : DP
        self.dp = [[None] * (2 ** 16) for _ in range(len(positions))]
        return self.traverse(-1, mask, positions, min_steps, corresponding_node)
    def traverse(self, knight_idx, mask, positions, min_steps, corresponding_node):
        if self.dp[knight_idx][mask] != None:
            return self.dp[knight_idx][mask]
        mask_is_even = self.is_even(mask)
        ans = float('-inf') if mask_is_even else float('inf')
        knight_node = corresponding_node[tuple(positions[knight_idx])]
        mask = mask | (1 << knight_node)
        for i in range(len(positions)):
            curr_i, curr_j = positions[i]
            if ((mask >> i) & 1) == 0:
                pawn_node = corresponding_node[(curr_i, curr_j)]
                steps = min_steps[pawn_node][knight_node]
                temp_ans = steps + self.traverse(i, mask, positions, min_steps, corresponding_node)
                if mask_is_even :
                    ans = max(ans, temp_ans)
                else:
                    ans = min(ans, temp_ans)
        mask = mask ^ (1 << knight_node)
        if ans == float('inf') or ans == float('-inf'):
            self.dp[knight_idx][mask] = 0
            return 0
        self.dp[knight_idx][mask] = ans
        return self.dp[knight_idx][mask]
    
    def is_even(self, mask):
        count = 0 
        for i in range(32):
            if ((mask >> i) & 1) == 1:
                count += 1
        return count % 2 == 0
    def helper(self, pos1, pos2):
        i1, j1 = pos1
        i2, j2 = pos2
        x = [-2, -2, -1, -1, 1, 1, 2, 2]
        y = [-1, 1, -2, 2, -2, 2, -1, 1]
        visited = [[False] * 50 for _ in range(50)]
        visited[i1][j1] = True
        dq = deque()
        dq.append((i1, j1, 0))
        while dq:
            curr_i, curr_j, curr_steps = dq.popleft()
            if curr_i == i2 and curr_j == j2:
                return curr_steps
            for direction in range(8):
                new_i = curr_i + x[direction]
                new_j = curr_j + y[direction]
                if new_i >= 0 and new_i < 50 and new_j >= 0 and new_j < 50 and visited[new_i][new_j] == False:
                    visited[new_i][new_j] = True
                    dq.append((new_i, new_j, curr_steps + 1))
        return -1