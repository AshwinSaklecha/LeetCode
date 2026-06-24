class Solution:
    def getDistances(self, nums: List[int]) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]].append(i)
            else:
                my_dict[nums[i]] = [i]
        ans = [0] * len(nums)
        for key in my_dict :
            ps = [0]
            for i in range(len(my_dict[key])):
                ps.append(ps[i] + my_dict[key][i])
            # ps is ready 
            curr_len = len(my_dict[key])
            for i in range(curr_len):
                idx = my_dict[key][i]
                curr_ans = (idx * i) - (idx * (curr_len - 1 - i)) 
                curr_ans -= (ps[i])
                curr_ans += (ps[curr_len] - ps[i+1])
                ans[idx] = curr_ans
        return ans
        