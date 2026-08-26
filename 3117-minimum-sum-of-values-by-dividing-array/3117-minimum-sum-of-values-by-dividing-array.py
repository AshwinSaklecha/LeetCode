class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        max_num = max(nums)
        self.dp = {}
        ans = self.traverse(0, 0, nums[0], nums, andValues)
        return -1 if ans == float('inf') else ans
    
    def traverse(self, i, j, curr_num, nums, andValues):
        if i >= len(nums) and j >= len(andValues):
            return 0
        if i >= len(nums) or j >= len(andValues):
            return float('inf')
        if (i, j, curr_num) in self.dp:
            return self.dp[(i, j, curr_num)]
        new_and = curr_num & nums[i]
        # case 1 : take it 
        path1 = self.traverse(i+1, j, new_and, nums, andValues)
        # case 2 : if new_and is equal, then we can move the j pointer 
        path2 = float('inf')
        if new_and == andValues[j]:
            new_and_val = -1 if i+1 >= len(nums) else nums[i+1]
            path2 = nums[i] + self.traverse(i+1, j+1, new_and_val, nums, andValues)

        self.dp[(i, j, curr_num)] = min(path1, path2)
        return self.dp[(i, j, curr_num)]