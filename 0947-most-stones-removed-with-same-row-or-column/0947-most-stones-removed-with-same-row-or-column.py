class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [i for i in range(len(stones))]
        rank = [0] * len(stones)
        print(parent)
        for i in range(len(stones)-1):
            for j in range(i+1, len(stones)):
                i1, j1 = stones[i]
                i2, j2 = stones[j]
                if i1 == i2 or j1 == j2:
                    self.union(i, j, rank, parent)
        my_dict = {}
        for i in range(len(parent)):
            node_parent = self.find(i, parent)
            if node_parent in my_dict :
                my_dict[node_parent] += 1
            else:
                my_dict[node_parent] = 1
        ans = 0
        for key in my_dict:
            ans += (my_dict[key] - 1)
        return ans
    def find(self, node, parent):
        # path compression
        if node == parent[node]:
            return node
        parent[node] = self.find(parent[node], parent)
        return parent[node]
    def union(self, node1, node2, rank, parent):
        # union by rank
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)

        if rank[parent1] > rank[parent2] :
            parent[parent2] = parent1
        elif rank[parent2] > rank[parent1]:
            parent[parent1] = parent2
        else:
            parent[parent1] = parent2
            rank[parent2] += 1