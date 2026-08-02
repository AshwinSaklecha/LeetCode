class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.dp = [[[None] * len(piles) for _ in range(len(piles))] for _ in range(2)]
        ans = self.traverse(0, len(piles)-1, True, piles)
        total = sum(piles)
        return ans > total - ans
    def traverse(self, i, j, is_alice, piles):
        if i > j :
            return 0
        alice_idx = 0 if is_alice else 1
        if self.dp[alice_idx][i][j] != None:
            return self.dp[alice_idx][i][j]
        if is_alice :
            self.dp[alice_idx][i][j] = max(
                piles[i] + self.traverse(i+1, j, not is_alice, piles),
                piles[j] + self.traverse(i, j-1, not is_alice, piles)
            )
            return self.dp[alice_idx][i][j]
        self.dp[alice_idx][i][j] = min(
            self.traverse(i+1, j, not is_alice, piles),
            self.traverse(i, j-1, not is_alice, piles)
        )
        return self.dp[alice_idx][i][j]