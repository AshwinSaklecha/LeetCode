class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        prev_num = -1
        self.dp = {}
        ans1 = self.traverse(0, prev_num, 0, nums)
        ans2 = self.traverse(0, prev_num, 1, nums)
        return max(ans1, ans2)
    
    def traverse(self, i, prev_num, remainder, nums):
        if prev_num != -1 :
            prev_num = prev_num % 2
        if i >= len(nums):
            return 0
        key_str = str(i) + "_" + str(prev_num) + "_" + str(remainder)
        if key_str in self.dp :
            return self.dp[key_str]
        take = 0
        if prev_num == -1 or (nums[i] + prev_num) % 2 == remainder :
            take = 1 + self.traverse(i+1, nums[i], remainder, nums)
        skip = self.traverse(i+1, prev_num, remainder, nums)

        self.dp[key_str] = max(take, skip)
        return self.dp[key_str]

        