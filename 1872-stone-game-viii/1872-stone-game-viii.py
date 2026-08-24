class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        self.dp = [None] * len(stones)
        ps = [stones[0]]
        for i in range(1, len(stones)):
            ps.append(ps[-1] + stones[i])
        ans = self.traverse(1, stones, ps)
        return ans
    
    def traverse(self, idx, stones, ps):
        if idx == len(stones)-1:
            return ps[idx]
        if self.dp[idx] != None:
            return self.dp[idx]
        take = ps[idx] - self.traverse(idx+1, stones, ps)
        skip = self.traverse(idx+1, stones, ps)
        self.dp[idx] = max(take, skip)
        return self.dp[idx]