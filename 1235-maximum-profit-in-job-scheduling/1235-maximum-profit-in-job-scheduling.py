class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        start_end_profit = []
        for i in range(len(startTime)):
            start_end_profit.append([startTime[i], endTime[i], profit[i]])
        
        start_end_profit.sort()
        self.dp = [None] * len(startTime)
        ans = self.traverse(0, start_end_profit)
        return ans
    
    def traverse(self, idx, sep): # sep short form of start_end_profit
        if idx >= len(sep) :
            return 0
        if self.dp[idx] != None :
            return self.dp[idx]
        new_idx = self.binary_search(sep[idx][1], sep)
        path1 = sep[idx][2] + self.traverse(new_idx, sep)
        path2 = self.traverse(idx + 1, sep)
        self.dp[idx] = max(path1, path2)
        return self.dp[idx]
    
    def binary_search(self, num, arr):
        idx = float('inf')
        s = 0 
        e = len(arr) - 1
        while s <= e :
            mid = (s + e) // 2 
            if arr[mid][0] >= num :
                idx = mid 
                e = mid - 1
            else :
                s = mid + 1
        
        return idx 
