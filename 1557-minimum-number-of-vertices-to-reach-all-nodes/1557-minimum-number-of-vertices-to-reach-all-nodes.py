class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # topo sort 
        topo = []
        indegree = [0] * n
        graph = [[] for _ in range(n)]
        for edge in edges :
            u,v = edge
            indegree[v] += 1
            graph[u].append(v)
        self.kahn(topo, n, graph, indegree)
        print(topo)
        visited = [False] * n
        ans = []
        for i in range(len(topo)):
            if visited[topo[i]] == False:
                ans.append(topo[i])
                self.dfs(topo[i], visited, graph)
        return ans
    
    def dfs(self, node, visited, graph):
        visited[node] = True
        for children in graph[node]:
            if visited[children] == False:
                self.dfs(children, visited, graph)
    def kahn(self, topo, n, graph, indegree):
        qu = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                qu.append(i)
        while qu :
            pop = qu.popleft()
            topo.append(pop)
            for children in graph[pop]:
                indegree[children] -= 1
                if indegree[children] == 0:
                    qu.append(children)
            

        