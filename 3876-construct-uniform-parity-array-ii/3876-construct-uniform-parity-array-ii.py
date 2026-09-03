class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        nums.sort()
        smallest_odd = float('inf')
        smallest_even = float('inf')

        for num in nums :
            if num % 2 == 0 :
                smallest_even = min(smallest_even, num)
            else:
                smallest_odd = min(smallest_odd, num)
        
        # first case, all ODDS
        flag_odd = True
        for i in range(len(nums)):
            if nums[i] % 2 == 0 :
                if smallest_odd != float('inf') and nums[i] - smallest_odd >= 1:
                    continue
                else:
                    flag_odd = False
                    break

        # first case, all EVENS
    
        flag_even = True
        for i in range(len(nums)):
            if nums[i] % 2 != 0 :
                if nums[i] - smallest_odd >= 1 :
                    continue 
                else:
                    flag_even = False
                    break
        return flag_odd or flag_even