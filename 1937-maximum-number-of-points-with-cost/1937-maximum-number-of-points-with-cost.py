class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        prev_max = points[0][:]
        for i in range(1, len(points)):
            l2r_max = deque() #moving from left to right ->
            r2l_max = deque() # <-

            # move left to right 
            for j in range(len(points[i])):
                max_val = prev_max[j]
                if j > 0 :
                    max_val = max(max_val, l2r_max[-1] - 1)
                l2r_max.append(max_val)
            
            # move from right to left 
            for j in range(len(points[i])-1, -1, -1):
                max_val = prev_max[j]
                if j < len(points[i])-1 :
                    max_val = max(max_val, r2l_max[0] - 1)
                r2l_max.appendleft(max_val)
            idx=0
            for max1, max2 in zip(l2r_max, r2l_max):
                prev_max[idx] = points[i][idx] + max(max1, max2)
                idx += 1
        
        return max(prev_max)