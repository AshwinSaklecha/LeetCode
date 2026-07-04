class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # apply normal dfs traversal
        self.ans = float('inf')
        graph = [[] for _ in range(n)]
        for path in roads :
            u, v, w = path 
            u -= 1
            v -= 1
            graph[u].append((v, w))
            graph[v].append((u, w))
        visited = [False] * n
        self.traverse(0, graph, visited)
        return self.ans
    def traverse(self, node, graph, visited):
        visited[node] = True
        for children in graph[node]:
            ch_node, ch_weight = children
            self.ans = min(self.ans, ch_weight)
            if visited[ch_node] == False:
                self.traverse(ch_node, graph, visited)