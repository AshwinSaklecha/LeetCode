class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        x = [0, -1, -1]
        y = [-1, -1, 0]
        squares = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                min_squares = float('inf')
                for direction in range(3):
                    new_i = i + x[direction]
                    new_j = j + y[direction]
                    if new_i < 0 or new_j < 0 or matrix[i][j] == 0:
                        min_squares = 0
                        break
                    min_squares = min(min_squares, squares[new_i][new_j])
                squares[i][j] = 1 + min_squares
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans += squares[i][j]
        return ans