class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(len(colors))]
        # indegree is created, for cycle detection and zero_indegree makup
        indegree = [0] * len(colors)
        for edge in edges :
            u, v = edge 
            graph[u].append(v)
            indegree[v] += 1
        
        # create the zero_indegree list
        zero_indegree = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero_indegree.append(i)
        

        # check if there is cycle
        topo = []
        is_cyclic = self.check(graph, indegree, topo)
        if is_cyclic :
            return -1
        
        ans = 1
        visited = [False] * len(graph)
        dp = [[0] * 26 for _ in range(len(graph))]

        for i in range(len(zero_indegree)):
            node = zero_indegree[i]
            self.dfs(node, graph, colors, dp, visited)

        # i think now the whole dp is complete 
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                ans = max(ans, dp[i][j])
        return ans

    def dfs(self, node, graph, colors, dp, visited):
        visited[node] = True
        for child in graph[node]:
            if visited[child] == False:
                self.dfs(child, graph, colors, dp, visited)
            for dp_idx in range(26):
                dp[node][dp_idx] = max(dp[node][dp_idx], dp[child][dp_idx])

        # after processing all children, mark curr_node color at the very end
        dp_idx = ord(colors[node]) - 97
        dp[node][dp_idx] += 1
            


    def check(self, graph, indegree, topo):
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
        return sum(indegree) > 0