class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # solved purely on basis of observations, not only on visualizations 
        smallest_idx = 0
        smallest_num = nums[0]
        for i in range(len(nums)):
            if nums[i] < smallest_num :
                smallest_num, smallest_idx = nums[i], i
        # check to right and check to left for increasing 
        flag1 = True # True means its possible 
        flag2 = True # True means its possible 
        prev_num = float('-inf')
        for idx in range(smallest_idx, smallest_idx + len(nums)):
            print(idx)
            idx = idx % len(nums)
            if nums[idx] > prev_num:
                prev_num = nums[idx]
            else :
                flag1 = False
                break
        prev_num = float('-inf')
        print("------------------")
        for idx in range(smallest_idx, smallest_idx - len(nums), -1):
            print(idx)
            if nums[idx] > prev_num:
                prev_num = nums[idx]
            else :
                flag2 = False
                break

        if flag1 :
            ans1 = smallest_idx 
            ans2 = 1 + 1 + len(nums) - 1 - smallest_idx + 1
            return min(ans1, ans2)
        if flag2:
            ans1 = len(nums) - 1 - smallest_idx + 1
            ans2 = smallest_idx + 1 + 1
            return min(ans1, ans2)
        return -1