class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph = [[] for _ in range(len(online))]
        for edge in edges :
            u, v, w = edge 
            graph[u].append((v, w))
        s = 0
        e = int(1e9)
        ans = self.binary_search(s, e, graph, online, k)
        return ans
    
    def binary_search(self, s, e, graph, online, k):
        ans = float('-inf')
        while s <= e:
            mid = (s + e ) // 2 
            if self.check(mid, graph, online, k):
                ans = mid 
                s = mid + 1
            else:
                e = mid - 1
        print(ans)
        return -1 if ans == float('-inf') else ans
    
    def check(self, val, graph, online, k):
        # apply disjkstra here with a little modification
        if online[0] == False or online[len(online) - 1] == False:
            return False
        heap = []
        min_weight = [float('inf')] * len(online)
        min_weight[0] = 0
        heapq.heappush(heap, (0, 0))  # weight, node
        while heap:
            curr_weight, curr_node = heapq.heappop(heap)
            if curr_weight > min_weight[curr_node]:
                continue
            for children in graph[curr_node]:
                ch_node, ch_weight = children
                if ch_weight < val or online[ch_node] == False:
                    continue
                new_weight = ch_weight + curr_weight
                if new_weight <= k and new_weight < min_weight[ch_node]:
                    min_weight[ch_node] = new_weight
                    heapq.heappush(heap, (new_weight, ch_node))
        return min_weight[-1] <= k