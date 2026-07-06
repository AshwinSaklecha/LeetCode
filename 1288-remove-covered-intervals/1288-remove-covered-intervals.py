class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def custom_sort(x):
            return x[0], -x[1]
        intervals.sort(key = custom_sort)
        if len(intervals) == 1:
            return len(intervals)
        ans = 0
        last_i, last_j = intervals[0]
        for i in range(1, len(intervals)):
            new_i, new_j = intervals[i]
            if last_i <= new_i and last_j >= new_j:
                ans += 1
            else:
                last_i, last_j = intervals[i]
        return len(intervals) - ans