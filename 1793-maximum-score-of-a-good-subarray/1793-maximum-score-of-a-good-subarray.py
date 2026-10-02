class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        i = k 
        j = k 
        min_num = nums[k]
        ans = nums[k]

        while i != len(nums) - 1 or j != 0 :
            if j - 1 >= 0 and i + 1 <= len(nums) - 1 :
                num1, num2 = nums[j-1], nums[i+1]
                if num1 > num2 :
                    j = j - 1
                    min_num = min(min_num, nums[j])
                else:
                    i = i + 1
                    min_num = min(min_num, nums[i])
            elif j == 0 :
                i = i + 1
                min_num = min(min_num, nums[i])
            else :
                j = j - 1 
                min_num = min(min_num, nums[j])
            ans = max(ans, min_num * (i-j+1))
        
        return ans