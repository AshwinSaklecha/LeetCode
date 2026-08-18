class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        if k == len(nums):
            return max(nums)
        if k == 1 :
            ans = -1
            my_dict = {}
            for num in nums:
                if num in my_dict:
                    my_dict[num] += 1
                else:
                    my_dict[num] = 1
            for key in my_dict:
                if my_dict[key] == 1 :
                    ans = max(ans, key)
            return ans
        if len(nums) == 2 :
            if k == 2 or nums[0] == nums[-1]:
                return -1
            return max(nums[0], nums[-1])
            
        num1 = nums[0]
        num2 = nums[-1]
        if num1 == num2 :
            num1 = -1
            num2 = -1
        # assuming nums length is greater than 3 
        for i in range(1, len(nums)-1):
            if nums[i] == num1 :
                num1 = -1
            if nums[i] == num2 :
                num2 = -1
        return max(num1, num2)