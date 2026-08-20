class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        ans = float('inf')
        k -= 1
        top_k_list = SortedList()
        remaining_list = SortedList()
        sum = 0
        i = 1 
        j = 1 
        while j < len(nums):
            while j - i > dist:
                if nums[i] in top_k_list:
                    top_k_list.remove(nums[i])
                    sum -= nums[i]
                    if len(remaining_list) > 0 :
                        popped = remaining_list.pop(0)
                        top_k_list.add(popped)
                        sum += popped
                elif nums[i] in remaining_list:
                    remaining_list.remove(nums[i])
                i += 1
            if len(top_k_list) < k :
                top_k_list.add(nums[j])
                sum += nums[j]
            else:
                remaining_list.add(nums[j])
                popped = top_k_list.pop(-1)
                remaining_list.add(popped)
                sum -= popped
                small_pop = remaining_list.pop(0)
                top_k_list.add(small_pop)
                sum += small_pop
            
            if j - i == dist:
                ans = min(ans, sum)
            j += 1
        
        ans += nums[0]
        return ans