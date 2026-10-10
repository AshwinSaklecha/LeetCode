class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            if heights[i] >= heights[i+1] :
                continue 
            else :
                diff = heights[i+1] - heights[i]
                if bricks >= diff:
                    bricks -= diff
                    heapq.heappush(heap, -diff)
                else:
                    if ladders == 0 :
                        return i
                    top_bricks_used = 0
                    if heap:
                        top_bricks_used = -(heap[0])
                    if top_bricks_used >= diff :
                        bricks += -(heapq.heappop(heap))
                        bricks -= diff
                        heapq.heappush(heap, -diff)
                    
                    ladders -= 1
        
        return len(heights) - 1