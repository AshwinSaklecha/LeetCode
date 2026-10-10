class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        heap = []
        my_dict = {}
        for i in range(len(nums1)):
            diff = abs(nums1[i]-nums2[i])
            if diff in my_dict :
                my_dict[diff] += 1
            else :
                my_dict[diff] = 1
        for key in my_dict :
            heapq.heappush(heap, (-key, my_dict[key]))
        ans = 0
        total_ops = k1 + k2 
        while total_ops > 0 and heap:
            key, val = heapq.heappop(heap)
            if key != 0 :
                total_freq = val
                while heap and heap[0][0] == key:
                    key2, val2 = heapq.heappop(heap)
                    total_freq += (val2)

                    
                if total_ops >= total_freq :
                    total_ops -= total_freq 
                    key += 1
                else :
                    unchanged = total_freq - total_ops 
                    heapq.heappush(heap, (key, unchanged))
                    total_freq = total_ops
                    key += 1
                    total_ops = 0
                if key != 0 :
                    heapq.heappush(heap, (key, total_freq))

        while heap :
            key, val = heapq.heappop(heap)
            ans += (int(key ** 2) * val)
        return ans
            
        