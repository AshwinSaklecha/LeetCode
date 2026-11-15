class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd_count = 0
        even_count = 0
        mod = int(1e9) + 7
        ans = 0
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum % 2 == 0 :
                ans = (ans + odd_count) % mod
                even_count += 1
            else :
                ans = (ans + 1 + even_count) % mod
                odd_count += 1
        return ans