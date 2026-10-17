class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i
        def custom_sort(x):
            sum = 0
            num = x
            while num > 0 :
                sum += (num % 10)
                num = num // 10
            return sum, x
        nums.sort(key=custom_sort)
        visited = [False] * len(nums)
        ans = 0
        for i in range(len(nums)):
            if visited[i]:
                continue
            idx = i
            swaps = 0
            while visited[idx] != True:
                visited[idx] = True
                swaps += 1
                idx = my_dict[nums[idx]]
            swaps -= 1
            ans += swaps
        return ans