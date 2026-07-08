class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False] * len(edges)
        recursion_stack = [[False, 0] for _ in range(len(edges))]
        ans = -1
        for i in range(len(edges)):
            if visited[i] == False:
                ans = max(ans, self.traverse(i, 0, edges, visited, recursion_stack))
        if ans == 0:
            return -1
        return ans
    def traverse(self, node, count, edges, visited, recursion_stack):
        if recursion_stack[node][0] == True:
            return count - recursion_stack[node][1]
        if edges[node] == -1:
            return -1
        if visited[node] == True:
            return -1
        visited[node] = True
        recursion_stack[node] = [True, count]
        ans = self.traverse(edges[node], count + 1, edges, visited, recursion_stack)
        recursion_stack[node] = [False, 0]
        return ans