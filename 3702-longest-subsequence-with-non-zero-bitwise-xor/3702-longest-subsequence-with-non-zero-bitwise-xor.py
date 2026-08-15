class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0 
        zero_count = 0
        for num in nums :
            if num == 0:
                zero_count += 1
            xor = xor ^ num
        if zero_count == len(nums):
            return 0
        if xor == 0:
            return len(nums) - 1
        return len(nums)