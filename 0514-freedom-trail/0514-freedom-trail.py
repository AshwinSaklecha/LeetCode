class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        self.dp = [[None] * len(key) for _ in range(len(ring))]
        my_dict = {}
        for i in range(len(ring)):
            if ring[i] in my_dict :
                my_dict[ring[i]].append(i)
            else:
                my_dict[ring[i]] = [i]
        

        ans = self.traverse(0, 0, my_dict, ring, key)
        return ans
    
    def traverse(self, i, j, my_dict, ring, key):
        if j >= len(key):
            return 0
        if self.dp[i][j] != None:
            return self.dp[i][j]
        path = float('inf')
        my_list = my_dict[key[j]]
        for idx in range(len(my_list)):
            diff = abs(my_list[idx] - i)
            min_dist = min(diff, len(ring) - diff)
            path = min(
                path, 
                min_dist + 1 + self.traverse(my_list[idx], j+1, my_dict, ring, key)
            )
        
        self.dp[i][j] = path
        return self.dp[i][j]