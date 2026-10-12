class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        ans = 0
        store = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 :
                    continue 
                else :
                    left_zeros = 1
                    up_zeros = 1
                    squares = 1
                    if j - 1 >= 0 :
                        if store[i][j-1] != None :
                            left_zeros += store[i][j-1][0]
                    if i - 1 >= 0 :
                        if store[i-1][j] != None :
                            up_zeros += store[i-1][j][1]
                    if i - 1 >= 0 and j-1 >= 0 :
                        if store[i-1][j-1] != None :
                            diagonal_squares = store[i-1][j-1][2] + squares
                            squares = min(diagonal_squares, left_zeros, up_zeros)
                    store[i][j] = [left_zeros, up_zeros, squares]
                    ans += squares
        
        return ans



        
        