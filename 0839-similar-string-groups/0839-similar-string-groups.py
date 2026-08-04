class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rank = [0] * len(strs)
        parent = [i for i in range(len(strs))]
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                str1 = strs[i]
                str2 = strs[j]
                if self.check(str1, str2):
                    self.union(i, j, rank, parent)
        my_set = set()
        for i in range(len(parent)):
            parent[i] = self.find(i, parent)
            my_set.add(parent[i])
        return len(my_set)
    
    def union(self, node1, node2, rank, parent):
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)

        if parent1 == parent2:
            return 
        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
        elif rank[parent1] < rank[parent2]:
            parent[parent1] = parent2
        else:
            parent[parent1] = parent2
            rank[parent2] += 1

    def find(self, node, parent):
        if parent[node] == node:
            return node
        parent[node] = self.find(parent[node], parent)
        return parent[node]
    def check(self, str1, str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
            if count > 2 :
                return False
        return True

            



        