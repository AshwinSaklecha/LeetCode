class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        if len(nums) == 1 :
            return 0
        nums.sort()
        mid_idx = len(nums) // 2
        mid_num = nums[mid_idx]
        another_num = nums[mid_idx - 1]

        ans1 = 0
        ans2 = 0
        for i in range(len(nums)):
            ans1 += abs(nums[i] - mid_num)
            ans2 += abs(nums[i] - another_num)
        
        return min(ans1, ans2)


        