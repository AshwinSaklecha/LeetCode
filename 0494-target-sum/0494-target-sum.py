class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        self.dp = {}
        ans = self.traverse(0, target, nums)
        return ans
    
    def traverse(self, idx, target, nums):
        if idx >= len(nums):
            if target == 0 :
                return 1
            return 0
        key_str = str(idx) + "_" + str(target)
        if key_str in self.dp :
            return self.dp[key_str]
        path1 = self.traverse(idx + 1, target - nums[idx], nums)
        path2 = self.traverse(idx + 1, target + nums[idx], nums)

        self.dp[key_str] = path1 + path2
        return self.dp[key_str] 