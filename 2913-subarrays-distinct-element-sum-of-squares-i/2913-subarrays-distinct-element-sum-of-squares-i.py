class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            my_set = set()
            for j in range(i, len(nums)):
                my_set.add(nums[j])
                ans += (len(my_set) ** 2)
        return ans