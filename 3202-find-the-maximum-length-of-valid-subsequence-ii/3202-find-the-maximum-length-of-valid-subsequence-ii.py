class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # bottom up has come to rescue 
        ans = 0
        dp = [[1] * len(nums) for _ in range(k)]
        for i in range(len(nums)):
            for j in range(i):
                mod_val = (nums[i] + nums[j]) % k
                dp[mod_val][i] = max(dp[mod_val][j] + 1, dp[mod_val][i])
                ans = max(ans, dp[mod_val][i])
        
        return ans