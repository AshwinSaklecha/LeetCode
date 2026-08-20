class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        is_cycle = [None] * len(graph)
        visited = [False] * len(graph)

        for node in range(len(graph)):
            if is_cycle[node] == None:
                self.dfs(node, graph, is_cycle, visited)
        ans = []
        for i in range(len(is_cycle)):
            if is_cycle[i] == False:
                ans.append(i)
        return ans
    
    def dfs(self, node, graph, is_cycle, visited):
        if visited[node] == True:
            is_cycle[node] = True
            visited[node] = False
            return True
        visited[node] = True
        is_there_cycle = False
        for child in graph[node]:
            if is_cycle[child] == None:
                self.dfs(child, graph, is_cycle, visited)
            is_there_cycle = is_there_cycle or is_cycle[child]
        
        visited[node] = False
        is_cycle[node] = is_there_cycle
        return is_there_cycle