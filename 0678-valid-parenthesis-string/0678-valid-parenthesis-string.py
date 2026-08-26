class Solution:
    def checkValidString(self, s: str) -> bool:
        self.dp = [[None] * len(s) for _ in range(len(s))]
        ans = self.traverse(0, 0, s)
        return ans
    
    def traverse(self, idx, brackets, s):
        if idx >= len(s):
            return brackets == 0
        if brackets < 0 :
            return False
        if self.dp[idx][brackets] != None:
            return self.dp[idx][brackets]
        path = None
        if s[idx] == "(":
            path = self.traverse(idx + 1, brackets + 1, s)
        elif s[idx] == ")":
            path = self.traverse(idx + 1, brackets - 1, s)
        else: #case for star
            path1 = self.traverse(idx+1, brackets + 1, s)
            path2 = self.traverse(idx + 1, brackets -1, s)
            path3 = self.traverse(idx + 1, brackets, s)

            path = path1 or path2 or path3
        
        self.dp[idx][brackets] = path
        return self.dp[idx][brackets]