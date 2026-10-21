class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        def custom_sort(x):
            return x[1], x[2]
        trips.sort(key=custom_sort)
        heap = []
        for chunk in trips :
            passen, _from, _to = chunk 
            heapq.heappush(heap, (_from, passen))
            heapq.heappush(heap, (_to, -passen))
        
        
        while heap:
            x, passengers_boarding = heapq.heappop(heap)
            capacity -= passengers_boarding
            if capacity < 0 :
                return False
        
        return True


            