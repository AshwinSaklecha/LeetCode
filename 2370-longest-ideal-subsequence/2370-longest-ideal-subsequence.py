class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        self.dp = [[None] * 27 for _ in range(len(s))]
        ans = self.traverse(0, -1, k, s)
        return ans
    
    def traverse(self, idx, prev_char, k, s):
        if idx >= len(s):
            return 0

        prev_char_idx = -1 if prev_char == -1 else (ord(prev_char) - 97)

        if self.dp[idx][prev_char_idx] != None:
            return self.dp[idx][prev_char_idx]
        
        # case 1 : skip 
        path1 = self.traverse(idx+1, prev_char, k, s)

        diff = self.calculate_diff(s, idx, prev_char)

        # case 2 : if s[idx] and prev_char diff is less than equal to k 
        path2 = 0
        if prev_char == -1 or (diff <= k):
            path2 = 1 + self.traverse(idx+1, s[idx], k, s)
        
        self.dp[idx][prev_char_idx] = max(path1, path2)
        return self.dp[idx][prev_char_idx]
    
    def calculate_diff(self, s, idx, prev_char):
        if prev_char == -1 :
            return 69
        num1 = ord(s[idx])
        num2 = ord(prev_char)
        return abs(num1 - num2)