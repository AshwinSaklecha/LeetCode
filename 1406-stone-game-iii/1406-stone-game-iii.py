class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.dp = [None] * len(stoneValue)
        ans = self.traverse(0, stoneValue)
        if ans == 0:
            return "Tie"
        return "Alice" if ans > 0 else "Bob"
    def traverse(self, i, stoneValue):
        if i >= len(stoneValue):
            return 0
        if self.dp[i] != None:
            return self.dp[i]
        result = float('-inf')
        pick1 = stoneValue[i] - self.traverse(i+1, stoneValue)
        result = max(result, pick1)
        if i + 1 < len(stoneValue):
            pick2 = stoneValue[i] + stoneValue[i+1] - self.traverse(i+2, stoneValue)
            result = max(result, pick2)
        if i + 2 < len(stoneValue):
            pick3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - self.traverse(i+3, stoneValue)
            result = max(result, pick3)
        self.dp[i] = result 
        return self.dp[i]
