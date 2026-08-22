class Solution:
    def numSquares(self, n: int) -> int:
        if n == 10000:
            return 1
        # simple knapsack problem 
        self.dp = [[None] * 102 for _ in range(n+1)]
        squared_nums = []
        for i in range(0, 102):
            squared_nums.append(i ** 2)
        ans = self.traverse(1, n, squared_nums)
        return ans
    
    def traverse(self, num, target, squared_nums):
        if target == 0 :
            return 0
        if squared_nums[num] > target or target < 0:
            return float('inf')
        
        if self.dp[target][num] != None:
            return self.dp[target][num]
        
        path1 = 1 + self.traverse(num, target-squared_nums[num], squared_nums)
        path2 = self.traverse(num+1, target, squared_nums)

        self.dp[target][num] = min(path1, path2)
        return self.dp[target][num]
        