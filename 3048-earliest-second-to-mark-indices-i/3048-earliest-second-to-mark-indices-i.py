class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        for i in range(len(changeIndices)):
            changeIndices[i] -= 1
        start_time = 0
        end_time = len(changeIndices) - 1
        ans = float('inf')
        while start_time <= end_time :
            mid = (start_time + end_time) // 2
            temp_nums = nums[:]
            if self.check(mid, temp_nums, changeIndices):
                ans = mid 
                end_time = mid - 1
            else :
                start_time = mid + 1
        return -1 if ans == float('inf') else ans + 1
    def check(self, time_idx, nums, change_indices):
        i = 0
        j = time_idx
        my_dict = {}
        marked_set = set() #indices from nums which are marked
        for idx in range(i, j+1):
            my_dict[change_indices[idx]] = idx
        if len(my_dict) < len(nums):
            return False
        
        index_last_occur = [] #(index last occurance in change_indices, nums index)
        for key in my_dict :
            heapq.heappush(index_last_occur, ([my_dict[key], key]))
        curr_target = heapq.heappop(index_last_occur)
        for idx in range(i, j+1):
            last_occurance_index_in_ci, nums_idx = curr_target
            nums[nums_idx] -= 1
            if nums[nums_idx] == -1 :
                marked_set.add(nums_idx)
                if index_last_occur:
                    curr_target = heapq.heappop(index_last_occur)
                else :
                    break
            elif idx == last_occurance_index_in_ci:
                break
        
        return len(marked_set) == len(nums)