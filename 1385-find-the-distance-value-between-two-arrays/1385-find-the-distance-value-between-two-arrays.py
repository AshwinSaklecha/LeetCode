class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        arr2 = SortedList(arr2)
        for num in arr1:
            idx = arr2.bisect_right(num)
            diff1 = abs(arr2[max(0, idx - 1)] - num)
            diff2 = abs(arr2[min(len(arr2) - 1, idx)] - num)

            if diff1 > d and diff2 > d :
                ans += 1
        
        return ans
            


