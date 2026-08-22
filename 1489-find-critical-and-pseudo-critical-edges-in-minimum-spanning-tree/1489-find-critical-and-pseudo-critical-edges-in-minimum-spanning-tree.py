class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # firstly add index to each node 
        for i in range(len(edges)):
            edges[i].append(i)
        print(edges)


        # now sort the edges 
        def custom_sort(x):
            return x[2]
        edges.sort(key=custom_sort)

        # find the total mst weight 
        mst_weight = self.calc_weight(edges, n, -1)


        # find critical edges 
        critical = []
        for i in range(len(edges)):
            popped = edges.pop(i)
            curr_weight = self.calc_weight(edges, n, -1)
            edges.insert(i, popped)
            if curr_weight > mst_weight : #then it was a critical edge
                critical.append(edges[i][-1])
        
        
        # critical is done, now find pseudo critical edges 
        # pseudo critical must not be in critical 
        pseudo_critical = []
        for i in range(len(edges)):
            if edges[i][-1] not in critical:
                weight_of_pseudo = self.calc_weight(edges, n, i)
                if weight_of_pseudo == mst_weight : #then it is pseudo critical 
                    pseudo_critical.append(edges[i][-1])

        ans = []
        ans.append(critical)
        ans.append(pseudo_critical)
        return ans 

    def calc_weight(self, edges, n, pseudo_num):
        total_weight = 0
        rank = [0] * n
        parent = [i for i in range(n)]
        if pseudo_num != -1 :
            u, v, w, idx = edges[pseudo_num]
            total_weight += w
            self.union(u, v, parent, rank)
        for i in range(len(edges)):
            u, v, w, idx = edges[i]
            p1 = self.find(u, parent)
            p2 = self.find(v, parent)
            if p1 != p2 :
                total_weight += w
                self.union(u, v, parent, rank)
        # final step, missed earlier, to check whether the graph is mst or not 
        my_set = set()
        for i in range(len(parent)):
            p1 = self.find(i, parent)
            my_set.add(p1)
        if len(my_set) > 1 :
            return float('inf') # means the mst was not even complete
        return total_weight

    def find(self, c1, parent):
        if parent[c1] == c1 :
            return c1
        parent[c1] = self.find(parent[c1], parent)
        return parent[c1]
    def union(self, c1, c2, parent, rank):
        p1 = self.find(c1, parent)
        p2 = self.find(c2, parent)

        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p1] < rank[p2]:
            parent[p1] = p2 
        else:
            parent[p1] = p2
            rank[p2] += 1
        