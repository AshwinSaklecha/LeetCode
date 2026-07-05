class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        self.mod = int(1e9) + 7
        self.dp = [[None] * len(board[0]) for _ in range(len(board))]
        i = len(board) - 1
        j = len(board[0]) - 1
        ans = self.traverse(i, j, board)
        if ans[0] == float('-inf'):
            return [0, 0]
        return ans
    def traverse(self, i, j, board):
        if i < 0 or j < 0 or board[i][j] == "X":
            return [float('-inf'), 0]
        if i == 0 and j == 0:
            return [0, 1]
        
        if self.dp[i][j] != None:
            return self.dp[i][j]
        max_score1, path1 = self.traverse(i-1, j, board)
        max_score2, path2 = self.traverse(i, j-1, board)
        max_score3, path3 = self.traverse(i-1, j-1, board)

        curr_num = 0
        if board[i][j] != "E" and board[i][j] != "X" and board[i][j] != "S":
            curr_num = int(board[i][j])
        max_score = max(max_score1, max_score2, max_score3)
        path = 0
        # 3 cases
        if max_score != float('-inf'):
            if max_score == max_score1:
                path = (path + path1) % self.mod
            if max_score == max_score2:
                path = (path + path2) % self.mod
            if max_score == max_score3:
                path = (path + path3) % self.mod
            max_score = (max_score + curr_num) % self.mod
        self.dp[i][j] = [max_score, path]
        return self.dp[i][j]