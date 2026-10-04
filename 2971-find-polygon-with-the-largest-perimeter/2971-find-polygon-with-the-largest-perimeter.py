class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total_sum = sum(nums)
        nums.reverse()
        for i in range(len(nums)-2) :
            if nums[i] < total_sum - nums[i] :
                return total_sum 
            else:
                total_sum -= nums[i]
        
        return -1