class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        self.dp = [[[None] * (len(s3) + 1) for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        ans = self.traverse(0, 0, 0, s1, s2, s3)
        return ans
    
    def traverse(self, i, j, k, s1, s2, s3):
        if k >= len(s3):
            if i >= len(s1) and j >= len(s2):
                return True
            return False
        
        if self.dp[i][j][k] != None:
            return self.dp[i][j][k]
        path1 = False 
        path2 = False 

        if i < len(s1) and s1[i] == s3[k] :
            path1 = self.traverse(i+1, j, k+1, s1, s2, s3)
        if j < len(s2) and s2[j] == s3[k] :
            path2 = self.traverse(i, j+1, k+1, s1, s2, s3)
        
        self.dp[i][j][k] = path1 or path2
        return self.dp[i][j][k]
        