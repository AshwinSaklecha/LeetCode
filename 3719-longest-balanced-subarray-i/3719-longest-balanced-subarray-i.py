class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            odd = 0
            even = 0
            my_set = set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0 and nums[j] not in my_set:
                    even += 1
                if nums[j] % 2 != 0 and nums[j] not in my_set:
                    odd += 1
                my_set.add(nums[j])
                if even == odd :
                    ans = max(ans, j - i + 1)
        return ans