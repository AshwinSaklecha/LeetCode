class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for edge in edges :
            u, v = edge 
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        return self.dfs(source, destination, visited, graph)
    def dfs(self, node, destiny, visited, graph):
        if node == destiny:
            return True
        visited[node] = True
        ans = False 
        for children in graph[node]:
            if visited[children] == False:
                ans = ans or self.dfs(children, destiny, visited, graph)
                if ans :
                    return ans
        return ans
        