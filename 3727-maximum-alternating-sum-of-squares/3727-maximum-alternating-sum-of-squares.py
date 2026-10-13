class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        def custom_sort(x):
            return abs(x)
        nums.sort(key=custom_sort)
        nums.reverse()
        ans = 0
        half = (len(nums) + 1) // 2 
        for i in range(half):
            ans += int(nums[i] ** 2)
        for i in range(half, len(nums)):
            ans -= int(nums[i] ** 2)
        
        return ans
        
        