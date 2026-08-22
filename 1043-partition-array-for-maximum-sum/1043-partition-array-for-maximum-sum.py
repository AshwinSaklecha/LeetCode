class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.dp = [None] * len(arr)
        ans = self.traverse(0, arr, k)
        return ans
    
    def traverse(self, idx, arr, k):
        if idx >= len(arr):
            return 0
        
        if self.dp[idx] != None:
            return self.dp[idx]
        
        ans = float('-inf')
        last_idx = min(len(arr) + 1, idx + k + 1)
        for i in range(idx+1, last_idx):
            temp_ans = self.get_max(arr, idx, i-1) + self.traverse(i, arr, k)
            ans = max(temp_ans, ans)
        self.dp[idx] = ans
        return self.dp[idx]

    def get_max(self, arr, s, e):
        max_num = max(arr[s:e+1])
        total_max = max_num * (e - s + 1)
        print(total_max)
        return total_max