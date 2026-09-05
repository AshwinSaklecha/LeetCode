class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_ps = []
        min_ps = []
        n = len(nums)-1

        for i in range(len(nums)):
            j = n - i
            if len(max_ps) == 0 :
                max_ps.append(nums[i])
                min_ps.append(nums[j])
            else:
                max_ps.append(max(max_ps[-1], nums[i]))
                min_ps.append(min(min_ps[-1], nums[j]))
        min_ps.reverse()

        for i in range(len(nums)):
            diff = max_ps[i] - min_ps[i]
            if diff <= k:
                return i
        return -1