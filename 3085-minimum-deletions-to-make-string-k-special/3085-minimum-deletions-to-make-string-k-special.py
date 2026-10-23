class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        my_dict = {}
        for char in word :
            if char in my_dict :
                my_dict[char] += 1
            else :
                my_dict[char] = 1
        nums = []
        for key in my_dict:
            nums.append(my_dict[key])
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)):
            steps = 0
            for idx in range(0, i):
                steps += nums[idx]
            x = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > x + k :
                    steps += (nums[j] - (x + k))
            ans = min(ans, steps)
        return ans

    