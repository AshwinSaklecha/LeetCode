class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        self.dp = [None] * len(nums)
        ans = self.traverse(0, nums, target)
        return -1 if ans == float('-inf') else ans
    def traverse(self, i, nums, target):
        if i >= len(nums):
            return float('-inf')
        if i == len(nums) - 1:
            return 0
        if self.dp[i] != None:
            return self.dp[i]
        ans = float('-inf')
        for j in range(i+1, len(nums)):
            if -target <= nums[j] - nums[i] <= target:
                ans = max(ans, 1 + self.traverse(j, nums, target))
        self.dp[i] = ans
        return self.dp[i]