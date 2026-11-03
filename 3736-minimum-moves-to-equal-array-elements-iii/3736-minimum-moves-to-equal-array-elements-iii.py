class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        ans = 0
        for num in nums :
            ans += (max_num - num)
        
        return ans

        