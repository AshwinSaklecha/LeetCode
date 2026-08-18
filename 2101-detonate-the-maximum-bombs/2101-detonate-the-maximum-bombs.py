class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # first create a graph 
        graph = [[] for _ in range(len(bombs))]
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j :
                    continue
                bomb1 = bombs[i]
                bomb2 = bombs[j]
                dist_from_center = self.calculate_dist(bomb1, bomb2)
                if bomb1[-1] >= dist_from_center :
                    graph[i].append(j)
        print(graph)
        ans = 1
        for i in range(len(graph)):
            ans = max(ans, self.bfs(i, graph))
        return ans
    
    def bfs(self, node, graph):
        max_dist = 0
        qu = deque()
        qu.append(node)
        visited = [False] * len(graph)
        visited[node] = True
        while qu:
            popped = qu.pop()
            max_dist += 1
            for child in graph[popped]:
                if visited[child] == True:
                    continue
                visited[child] = True
                qu.append(child)
        return max_dist

    def calculate_dist(self, bomb1, bomb2):
        x1, y1, r1 = bomb1
        x2, y2, r2 = bomb2
        dist = ((x2-x1) ** 2 + (y2-y1) ** 2 ) ** 0.5
        return dist
