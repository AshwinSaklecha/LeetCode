class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # not even in my dreams i could have come up with such approach 
        # i need more practice with bit manipulation
        mod = int(1e9) + 7
        one_list = []
        ans = 0
        for i in range(32):
            ones_count = 0
            for num in nums :
                if (num >> i) & 1 == 1 :
                    ones_count += 1
            one_list.append(ones_count)
        print(one_list)
        for i in range(k):
            curr_num = 0
            for j in range(32):
                if one_list[j] > 0 :
                    curr_num += (2 ** j)
                    one_list[j] -= 1
            ans = (ans + (curr_num ** 2 )) % mod
        
        return ans



