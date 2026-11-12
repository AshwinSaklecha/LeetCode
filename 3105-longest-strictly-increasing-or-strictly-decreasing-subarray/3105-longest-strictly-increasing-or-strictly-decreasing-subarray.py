class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans, i, j = 1, 0, 0
        while j < len(nums):
            if i == j :
                j += 1
            elif nums[j] > nums[j-1] :
                ans = max(ans, j - i + 1)
                j += 1
            else :
                i = j
        i, j = 0, 0
        while j < len(nums):
            if i == j :
                j += 1
            elif nums[j] < nums[j-1] :
                ans = max(ans, j - i + 1)
                j += 1
            else :
                i = j
        return ans