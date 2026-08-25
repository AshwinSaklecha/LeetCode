class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        my_set = set()
        for num in nums:
            if num % k == 0 :
                my_set.add(num)
        for i in range(1, len(my_set) + 2):
            if k * i not in my_set:
                return k * i
        return 69
