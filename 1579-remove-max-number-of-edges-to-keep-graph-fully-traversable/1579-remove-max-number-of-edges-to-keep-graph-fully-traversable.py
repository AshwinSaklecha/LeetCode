class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        rank = [0] * n
        parent = [i for i in range(n)]
        for edge in edges:
            # first do for both 
            turn, u, v = edge 
            u -= 1
            v -= 1
            if turn == 3 :
                parent_u = self.find(u, parent)
                parent_v = self.find(v, parent)
                if parent_u == parent_v :
                    ans += 1
                else:
                    self.union(u, v, parent, rank)
        rank_alice = rank[:]
        parent_alice = parent[:]
        rank_bob = rank[:]
        parent_bob = parent[:]

        for edge in edges :
            turn, u, v = edge 
            u -= 1
            v -= 1
            if turn == 1 :
                parent_u = self.find(u, parent_alice)
                parent_v = self.find(v, parent_alice)
                if parent_u == parent_v :
                    ans += 1
                else:
                    self.union(u, v, parent_alice, rank_alice)
            if turn == 2 :
                parent_u = self.find(u, parent_bob)
                parent_v = self.find(v, parent_bob)
                if parent_u == parent_v :
                    ans += 1
                else:
                    self.union(u, v, parent_bob, rank_bob)
            
        ultimate_alice = self.find(0, parent_alice)
        ultimate_bob = self.find(0, parent_bob)

        for i in range(len(parent_alice)):
            my_parent = self.find(i, parent_alice)
            if my_parent != ultimate_alice:
                return -1
        for i in range(len(parent_bob)):
            my_parent = self.find(i, parent_bob)
            if my_parent != ultimate_bob:
                return -1

        return ans
    
    def union(self, node1, node2, parent, rank):
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)

        if parent1 == parent2:
            return 
        
        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
        elif rank[parent1] < rank[parent2]:
            parent[parent1] = parent2
        else:
            parent[parent2] = parent1
            rank[parent1] += 1
    def find(self, node, parent):
        if node == parent[node]:
            return node
        parent[node] = self.find(parent[node], parent)
        return parent[node]

        