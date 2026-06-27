class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 0
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
        
        for key in my_dict:
            if my_dict[key] >= 2 and (key ** 2) in my_dict:
                continue
            else:
                num = key 
                temp_ans = 1
                root_num_float = num ** (0.5)
                num = round(root_num_float)
                if abs(root_num_float - num) > 0.001:
                    num = -1
                while num in my_dict and my_dict[num] >= 2:
                    temp_ans += 2
                    root_num_float = num ** (0.5)
                    num = round(root_num_float)
                    if abs(root_num_float - num) > 0.001:
                        num = -1
                ans = max(temp_ans, ans)
        
        if 1 in my_dict:
            ones = my_dict[1]
            if ones % 2 == 0:
                ones = ones - 1
            ans = max(ans, ones)
        return ans