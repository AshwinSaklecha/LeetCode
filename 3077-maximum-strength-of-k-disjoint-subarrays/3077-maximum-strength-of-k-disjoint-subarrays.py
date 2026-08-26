class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        self.dp = [[[None] * (k + 1) for _ in range(len(nums))] for _ in range(2)]
        ans = self.traverse(0, k, True, nums)
        return ans
    # previously was using i, j, k
    # now gonna optimize it using Add as you go trick 
    def traverse(self, i, k, is_new_subarr, nums):
        # some base conditions 
        if k == 0 :
            return 0
        if i >= len(nums):
            return float('-inf')

        is_new_subarr_idx = 0 if is_new_subarr else 1

        if self.dp[is_new_subarr_idx][i][k] != None:
            return self.dp[is_new_subarr_idx][i][k]

        multiplier = k if k % 2 != 0 else -k
        
        # case 1 : not take and skip, we cant run it always 
        path1 = float('-inf')
        if is_new_subarr:
            path1 = self.traverse(i+1, k, True, nums)
        # case 2 : take and skip 
        path2 = (multiplier * (nums[i])) + self.traverse(i+1, k-1, True, nums)
        # case 3 : take 
        path3 = (multiplier * (nums[i])) + self.traverse(i+1, k, False, nums)

        self.dp[is_new_subarr_idx][i][k] = max(path1, path2, path3)
        return self.dp[is_new_subarr_idx][i][k]