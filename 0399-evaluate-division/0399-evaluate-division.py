class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        my_dict = {}
        counter = 0
        for i in range(len(equations)):
            node1, node2 = equations[i]
            if node1 not in my_dict:
                my_dict[node1] = counter
                counter += 1
            if node2 not in my_dict:
                my_dict[node2] = counter
                counter += 1
        graph = [[] for _ in range(counter)]
        for i in range(len(equations)):
            char1, char2 = equations[i]
            node1, node2 = my_dict[char1], my_dict[char2]
            val = values[i]
            resip_val = 1 / val
            graph[node1].append([node2, val])
            graph[node2].append([node1, resip_val])
        ans = []
        for query in queries :
            char1, char2 = query
            if char1 not in my_dict or char2 not in my_dict:
                ans.append(float(-1))
                continue
            if char1 == char2 :
                ans.append(float(1))
                continue
            node1, node2 = my_dict[char1], my_dict[char2]
            visited = [False] * len(graph)
            temp_ans = self.dfs(node1, node2, graph, visited)
            temp_ans = float(-1) if temp_ans == float('-inf') else temp_ans
            ans.append(temp_ans)
        return ans
    
    def dfs(self, node1, node2, graph, visited):
        if node1 == node2:
            return 1
        visited[node1] = True
        for children, val in graph[node1]:
            if visited[children] == False:
                answer = self.dfs(children, node2, graph, visited)
                if answer != float('-inf'):
                    return val * answer
        return float('-inf')