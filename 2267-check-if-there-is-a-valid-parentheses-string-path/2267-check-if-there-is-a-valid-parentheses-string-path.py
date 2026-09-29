class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        self.dp = [[[None] * (len(grid) + len(grid[0])) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = self.traverse(0, 0, 0, grid)
        return ans
    
    def traverse(self, i, j, num, grid):
        if num < 0 :
            return False
        if i == len(grid) - 1 and j == len(grid[0]) - 1 :
            if grid[i][j] == ")" :
                num -= 1
                if num == 0 :
                    return True
            return False
        if i >= len(grid) or j >= len(grid[0]):
            return False
        
        # ------------------


        if grid[i][j] == "(":
            num += 1
        else :
            num -= 1
            
        if self.dp[i][j][num] != None:
            return self.dp[i][j][num]
        
        path1 = self.traverse(i+1, j, num, grid)
        path2 = self.traverse(i, j+1, num, grid)

        self.dp[i][j][num] = path1 or path2
        return self.dp[i][j][num]

        