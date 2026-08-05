class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        query_copy = [row[:] for row in queries]
        def custom_sort(x):
            return x[2]
        queries.sort(key=custom_sort)
        edgeList.sort(key=custom_sort)
        ans = []
        rank = [0] * n
        parent = [i for i in range(n)]
        dict_ans = {}
        idx = 0 
        for query in queries:
            start_node, dest_node, threshold = query
            while idx < len(edgeList) and edgeList[idx][2] < threshold:
                u, v, w = edgeList[idx]
                if w < threshold:
                    self.union(u, v, parent, rank)
                idx += 1
            comp1 = self.find(start_node, parent)
            comp2 = self.find(dest_node, parent)
            dict_ans[tuple(query)] = (comp1 == comp2)
        
        for query in query_copy:
            ans.append(dict_ans[tuple(query)])
        return ans

    def union(self, node1, node2, parent, rank):
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)
        if parent1 == parent2:
            return 
        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
        elif rank[parent2] > rank[parent1]:
            parent[parent1] = parent2
        else:
            parent[parent1] = parent2
            rank[parent2] += 1
    def find(self, node, parent):
        if parent[node] == node:
            return parent[node]
        parent[node] = self.find(parent[node], parent)
        return parent[node]