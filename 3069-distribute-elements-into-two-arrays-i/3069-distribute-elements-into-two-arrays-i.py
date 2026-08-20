class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i in range(len(nums)):
            if len(arr1) == 0:
                arr1.append(nums[i])
            elif len(arr2) == 0:
                arr2.append(nums[i])
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])
        return arr1 + arr2

        