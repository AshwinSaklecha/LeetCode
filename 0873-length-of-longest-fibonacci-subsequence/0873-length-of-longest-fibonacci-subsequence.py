class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        my_dict = {}
        ans = 0
        self.dp = [[None] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            my_dict[arr[i]] = i
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr) - 1) :
                temp_ans = self.traverse(i, j, arr, my_dict)
                ans = max(ans, temp_ans)
        
        return 0 if ans == 0 else ans + 2
    
    def traverse(self, i, j, arr, my_dict):
        if self.dp[i][j] != None :
            return self.dp[i][j]
        to_find = arr[i] + arr[j]
        if to_find not in my_dict :
            self.dp[i][j] = 0
            return self.dp[i][j]
        self.dp[i][j] = 1 + self.traverse(j, my_dict[to_find], arr, my_dict)
        return self.dp[i][j]