class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if i+1 != nums[i]:
                return False
        return nums[-1] == len(nums) - 1