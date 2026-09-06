class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.dp = [[None] * len(t) for _ in range(len(s))]
        ans = self.traverse(0, 0, s, t)
        return ans
    
    def traverse(self, i, j, s, t):
        if j >= len(t):
            return 1
        if i >= len(s):
            return 0
        if self.dp[i][j] != None:
            return self.dp[i][j]
        path1 = 0 
        if s[i] == t[j] :
            path1 = self.traverse(i+1, j+1, s, t)
        path2 = self.traverse(i+1, j, s, t)

        self.dp[i][j] = path1 + path2
        return self.dp[i][j]