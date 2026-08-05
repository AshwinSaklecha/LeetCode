class Solution:
    def remainingMethods(self, n: int, k: int, adj: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in adj:
            graph[u].append(v)
        marked = [False] * n
        self.dfs(k, marked, graph)
        for edge in adj:
            u, v = edge 
            if marked[u] == False and marked[v] == True:
                return [i for i in range(n)]
        ans = []
        for i in range(len(marked)):
            if marked[i] == False:
                ans.append(i)
        return ans
    def dfs(self, node, marked, graph):
        marked[node] = True
        for children in graph[node]:
            if marked[children] == False:
                self.dfs(children, marked, graph)