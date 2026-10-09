class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums) + 1
        self.dp = [[[None] * n for _ in range(n)] for _ in range(n)]
        ans = self.traverse(0, op1, op2, k, nums)
        return ans
    
    def traverse(self, idx, op1, op2, k, nums):
        if op1 < 0 or op2 < 0 :
            return float('inf')
        if idx >= len(nums):
            return 0
        
        if self.dp[idx][op1][op2] != None:
            return self.dp[idx][op1][op2]
        op1_num = (int(nums[idx] + 1) // 2)
        op2_num = None
        
        path1 = op1_num + self.traverse(idx + 1, op1 - 1, op2, k, nums)
        path2 = float('inf')
        path3 = float('inf')
        path4 = float('inf')
        if nums[idx] >= k:
            op2_num = nums[idx] - k
            path2 = op2_num + self.traverse(idx + 1, op1, op2 - 1, k, nums)
            path3 = (int(op2_num + 1) // 2) + self.traverse(idx + 1, op1 -1, op2 - 1, k, nums)
        if op1_num >= k :
            op2_num = op1_num - k
            path4 = op2_num + self.traverse(idx + 1, op1 -1, op2 - 1, k, nums)
        path5 = nums[idx] + self.traverse(idx + 1, op1, op2, k, nums)
        
        self.dp[idx][op1][op2] = min(path1, path2, path3, path4, path5)
        return self.dp[idx][op1][op2]
        