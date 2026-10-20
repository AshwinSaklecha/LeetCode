class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        self.dp = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        ans = float('inf')
        for j in range(len(matrix[0])):
            temp_ans = matrix[0][j] + min(self.traverse(1, j-1, matrix), self.traverse(1, j+1, matrix), self.traverse(1, j, matrix))
            ans = min(ans, temp_ans)
        return ans
    
    def traverse(self, i, j, matrix):
        if i >= len(matrix) :
            return 0
        if j < 0 or j >= len(matrix[0]):
            return float('inf')
        
        if self.dp[i][j] != None:
            return self.dp[i][j]
        path1 = self.traverse(i+1, j, matrix)
        path2 = self.traverse(i+1, j-1, matrix)
        path3 = self.traverse(i+1, j+1, matrix)
        self.dp[i][j] = matrix[i][j] + min(path1, path2, path3)
        return self.dp[i][j]
        