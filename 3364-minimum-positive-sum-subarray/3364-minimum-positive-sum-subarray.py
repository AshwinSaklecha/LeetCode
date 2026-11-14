class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        sum = float('inf')
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if l <= j - i + 1 <= r and curr_sum > 0:
                    sum = min(sum, curr_sum)
        return sum if sum != float('inf') else -1