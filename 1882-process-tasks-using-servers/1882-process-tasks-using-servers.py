class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        cool_down = []
        heap = []
        for i in range(len(servers)):
            heapq.heappush(cool_down, (0, servers[i], i))
        ans = []
        for idx in range(len(tasks)):
            self.transfer(cool_down, heap, idx)
            if len(heap) == 0 :
                start_time, weight, i = heapq.heappop(cool_down)
                ans.append(i)
                start_time += tasks[idx]
                heapq.heappush(cool_down, (start_time, weight, i))
            else:
                weight, i = heapq.heappop(heap)
                ans.append(i)
                start_time = tasks[idx] + idx
                heapq.heappush(cool_down, (start_time, weight, i))
        
        return ans
    def transfer(self, cool_down, heap, idx):
        while cool_down and cool_down[0][0] <= idx:
            _, weight, i = heapq.heappop(cool_down)
            heapq.heappush(heap, (weight, i))