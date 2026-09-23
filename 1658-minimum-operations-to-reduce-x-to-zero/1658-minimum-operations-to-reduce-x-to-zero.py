class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        size = 0 
        i = 0 
        j = 0 
        total_sum = sum(nums)
        required_sum = total_sum - x
        if required_sum < 0 :
            return -1
        if required_sum == 0 :
            return len(nums)

        while j < len(nums):
            required_sum -= nums[j]
            while required_sum <= 0:
                if required_sum == 0 :
                    size = max(size, j - i + 1)
                required_sum += nums[i]
                i += 1
            j += 1
        return -1 if size == 0 else len(nums) - size 