class Solution:
    def minOperations(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums :
            if num in my_dict :
                my_dict[num] += 1
            else :
                my_dict[num] = 1
        ans = 0
        for key in my_dict:
            if my_dict[key] % 3 == 0 :
                ans += (my_dict[key] // 3)
            elif my_dict[key] == 1 :
                return -1
            else :
                new_num = my_dict[key] - 2
                three_count = new_num // 3 
                remaining_num = my_dict[key] - (3 * three_count)
                two_count = remaining_num // 2 
                ans += (three_count + two_count)
        print(my_dict)
        return ans