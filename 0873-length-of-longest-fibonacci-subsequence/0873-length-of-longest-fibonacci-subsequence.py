class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        my_dict = {}
        ans = 0
        for i in range(len(arr)):
            my_dict[arr[i]] = i
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr) - 1) :
                temp_ans = self.traverse(i, j, arr, my_dict)
                ans = max(ans, temp_ans)
        
        return 0 if ans == 0 else ans + 2
    
    def traverse(self, i, j, arr, my_dict):
        to_find = arr[i] + arr[j]
        if to_find not in my_dict :
            return 0
        return 1 + self.traverse(j, my_dict[to_find], arr, my_dict)