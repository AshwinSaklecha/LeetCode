class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, int(n ** 0.5) + 1):
            print(i)
            if n % i == 0 :
                flag1 = self.check(nums, i)
                flag2 = False
                if n != i*i :
                    flag2 = self.check(nums, int(n // i))  
                if flag1 :
                    ans += i
                if flag2:
                    ans += (n // i)
        return ans

    def check(self, nums, subarr_size):
        print(f"these are subarr sizes that came : {subarr_size}")
        idx = 0
        prev_largest = 0
        while idx < len(nums):
            # now iterate subarr_size inside here 
            val = self.sub_check(nums, idx, idx+subarr_size-1, prev_largest)
            # [True/False, curr_largest]
            if val[0] == False:
                return False
            prev_largest = val[1]
            idx += subarr_size
        print(f"this is subarr size : {subarr_size}")
        return True
    
    def sub_check(self, nums, i, j, prev_largest):
        initial_i = i
        curr_smallest = nums[j]
        curr_largest = nums[j]
        inc_count = 0
        while i < j :
            if nums[i] > nums[i+1]:
                inc_count += 1
                if inc_count > 1:
                    return False, 69
            if inc_count > 0: 
                if nums[i+1] > nums[initial_i]:
                    return False, 69
            curr_smallest = min(curr_smallest, nums[i])
            curr_largest = max(curr_largest, nums[i])
            i += 1
        if curr_smallest < prev_largest :
            return False, 69
        return True, curr_largest