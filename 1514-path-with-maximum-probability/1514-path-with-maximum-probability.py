class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v =  edges[i]
            w = succProb[i]
            graph[u].append([v, w])
            graph[v].append([u, w])
        max_probab = [0] * n
        max_probab[start] = 1
        heap = []
        heapq.heappush(heap, (-1, start))
        while heap:
            pop = heapq.heappop(heap)
            probab, node = pop
            probab = -probab
            if max_probab[node] > probab :
                continue
            for children in graph[node]:
                ch_node, ch_wt = children
                new_probab = probab * ch_wt 
                if new_probab > max_probab[ch_node]:
                    max_probab[ch_node] = new_probab
                    heapq.heappush(heap, (-new_probab, ch_node))
        return max_probab[end]