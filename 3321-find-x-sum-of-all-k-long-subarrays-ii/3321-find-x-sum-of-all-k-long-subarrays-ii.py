class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        my_dict = {}

        # create two sortedSet(orderedset), one contains the top k elements, another contains the remaining elements

        top_x_set = SortedSet()
        remaining_set = SortedSet()
        ans = 0
        final_ans_list = []
        i = 0
        j = 0 
        while j < len(nums):
            # shrink the window first , this should be the first step
            while j - i >= k:
                # remove from dictionary, remove from set, if set is top_x then add from remaining, subtract the answer, add in the answer
                to_be_removed = (my_dict[nums[i]], nums[i])
                if to_be_removed in top_x_set :
                    top_x_set.remove(to_be_removed)
                    ans -= (to_be_removed[0] * to_be_removed[1])
                    my_dict[nums[i]] -= 1
                    if my_dict[nums[i]] != 0 :
                        if len(remaining_set) == 0:
                            top_x_set.add((my_dict[nums[i]], nums[i]))
                            ans += (my_dict[nums[i]] * nums[i])
                        elif my_dict[nums[i]] > remaining_set[-1][0] or (my_dict[nums[i]] == remaining_set[-1][0] and nums[i] >= remaining_set[-1][1]):
                            top_x_set.add((my_dict[nums[i]], nums[i]))
                            ans += (my_dict[nums[i]] * nums[i])
                        else:
                            remaining_set.add((my_dict[nums[i]], nums[i]))
                            to_add = remaining_set.pop(-1)
                            top_x_set.add(to_add)
                            ans += (to_add[0] * to_add[1])
                    else:
                        if len(remaining_set) != 0:
                            to_add = remaining_set.pop(-1)
                            top_x_set.add(to_add)
                            ans += (to_add[0] * to_add[1])
                else:
                    remaining_set.remove(to_be_removed)
                    my_dict[nums[i]] -= 1
                    if my_dict[nums[i]] != 0 :
                        remaining_set.add((my_dict[nums[i]], nums[i]))
                    else:
                        my_dict.pop(nums[i])
                i += 1
            
            if nums[j] in my_dict :
                # pick it from the set 
                if (my_dict[nums[j]], nums[j]) in top_x_set :
                    top_x_set.remove((my_dict[nums[j]], nums[j]))
                    ans -= (my_dict[nums[j]] * nums[j])
                else:
                    if (my_dict[nums[j]], nums[j]) in remaining_set:
                        remaining_set.remove((my_dict[nums[j]], nums[j]))
                my_dict[nums[j]] += 1
            else:
                my_dict[nums[j]] = 1
            # so we have got the nums[j] out of the set and updated the dict
            # now time to put it back 
            if len(top_x_set) < x:
                top_x_set.add((my_dict[nums[j]], nums[j])) 
                ans += (my_dict[nums[j]] * nums[j])
            else:
                x_set_compare = top_x_set[0]
                if my_dict[nums[j]] > x_set_compare[0] or (my_dict[nums[j]] == x_set_compare[0] and nums[j] >= x_set_compare[1]) :
                    top_x_set.pop(0)
                    ans -= (x_set_compare[0] * x_set_compare[1])
                    top_x_set.add((my_dict[nums[j]], nums[j])) 
                    ans += (my_dict[nums[j]] * nums[j])
                    remaining_set.add(x_set_compare)
                else:
                    remaining_set.add((my_dict[nums[j]], nums[j]))
            if j - i + 1 == k:
                final_ans_list.append(ans)
            j += 1
        return final_ans_list
        