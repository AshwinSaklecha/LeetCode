class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            curr_gcd = None 
            curr_lcm = None
            for j in range(i, len(nums)):
                if curr_gcd == None :
                    curr_gcd = nums[j]
                    curr_lcm = nums[j]
                else:
                    curr_gcd = math.gcd(curr_gcd, nums[j])
                    curr_lcm = math.lcm(curr_lcm, nums[j])
                curr_prod = math.prod(nums[i:j+1])
                if curr_prod == curr_lcm * curr_gcd :
                    ans = max(ans, j - i + 1)
        return ans

        