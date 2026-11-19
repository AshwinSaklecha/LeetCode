class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        case1, case2, case3 = float('inf'), float('inf'), float('inf'),
        nums.sort()
        small_count = 0
        big_count = 0
        for i in range(len(nums)):
            if nums[i] == nums[0] :
                small_count += 1
            if nums[i] == nums[-1]:
                big_count += 1
        # case 1 :
        if small_count <= 2 :
            case1 = nums[-1] - nums[2]
        else :
            case1 = nums[-1] - nums[0]

        # case 2 :
        if big_count <= 2 :
            case2 = nums[-3] - nums[0]
        else :
            case2 = nums[-1] - nums[0]

        # case 3 :
        if big_count == 1 and small_count == 1:
            case3 = nums[-2] - nums[1]
        return min(case1, case2, case3)