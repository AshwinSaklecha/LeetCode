class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) < 1:
            return 0
        graph = [[] for _ in range(n)]
        ans = 0
        degree = [0] * n
        for edge in roads:
            u, v = edge 
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        for i in range(len(degree)-1):
            for j in range(i+1, len(degree)):
                score = degree[i] + degree[j]
                for node in graph[i]:
                    if node == j:
                        score -= 1
                ans = max(ans, score)
        return ans