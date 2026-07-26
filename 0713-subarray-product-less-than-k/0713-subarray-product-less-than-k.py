class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        product = 1
        ans = 0
        i = 0
        j = 0 
        while j < len(nums):
            product = product * nums[j]
            while product >= k:
                product = product // nums[i]
                i += 1
            if product < k :
                ans += (j - i + 1)
            j += 1
        return ans