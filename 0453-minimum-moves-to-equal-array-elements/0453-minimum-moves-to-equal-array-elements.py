class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            ans += (nums[i]-nums[0])
        return ans
