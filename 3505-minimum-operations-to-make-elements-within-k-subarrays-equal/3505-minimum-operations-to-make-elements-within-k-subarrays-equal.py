from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        self.dp = {}
        max_steps_taken = self.build_max_steps_taken(nums, x, k)
        ans = self.traverse(0, k, x, max_steps_taken)
        return ans
    def build_max_steps_taken(self, nums, x, k):
        max_steps_taken = []
        sum_first = 0
        sum_second = 0
        first_half = SortedList()
        second_half = SortedList()
        i = 0 
        j = 0 
        while j < len(nums):
            if len(first_half) == 0 or nums[j] <= first_half[-1]:
                first_half.add(nums[j])
                sum_first += nums[j]
            else :
                second_half.add(nums[j])
                sum_second += nums[j]
            while len(second_half) > len(first_half):
                popped = second_half.pop(0)
                first_half.add(popped)
                sum_first, sum_second = sum_first + popped, sum_second - popped
            
            while len(first_half) - 1 > len(second_half):
                popped = first_half.pop()
                second_half.add(popped)
                sum_first, sum_second = sum_first - popped, sum_second + popped


            if j - i + 1 == x :
                # do computations
                median = first_half[-1]
                sum1 = abs((median * len(first_half)) - sum_first)
                sum2 = abs((median * len(second_half))- sum_second)
                max_steps_taken.append(sum1+sum2)
                if nums[i] in first_half:
                    first_half.remove(nums[i])
                    sum_first -= nums[i]
                else :
                    second_half.remove(nums[i])
                    sum_second -= nums[i]
                i += 1
            j += 1
        return max_steps_taken
    def traverse(self, i, k, x, max_steps_taken):
        if k == 0:
            return 0
        if i >= len(max_steps_taken):
            return float('inf')
        key_str = str(i) + "_" + str(k)
        if key_str in self.dp :
            return self.dp[key_str]
        take = max_steps_taken[i] + self.traverse(i+x, k-1, x, max_steps_taken)
        skip = self.traverse(i+1, k, x, max_steps_taken)
        self.dp[key_str] = min(take, skip)
        return self.dp[key_str]