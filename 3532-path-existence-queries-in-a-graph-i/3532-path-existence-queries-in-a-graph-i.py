class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            return [True] * len(queries)
        ans = []
        parent = [i for i in range(n)]
        rank = [0] * n
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= maxDiff:
                self.union(i, i-1, parent, rank)
        for query in queries:
            i, j = query 
            parent_i = self.find(i, parent)
            parent_j = self.find(j, parent)
            ans.append(parent_i == parent_j)
        return ans
    def find(self, node, parent):
        if node == parent[node]:
            return node
        parent[node] = self.find(parent[node], parent)
        return parent[node]
    def union(self, node1, node2, parent, rank):
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)

        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
        elif rank[parent2] > rank[parent1]:
            parent[parent1] = parent2
        else:
            parent[parent2] = parent1
            rank[parent1] += 1