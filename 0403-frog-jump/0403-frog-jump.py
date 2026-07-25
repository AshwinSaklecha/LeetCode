class Solution:
    def canCross(self, stones: List[int]) -> bool:
        my_dict = {}
        for i in range(len(stones)):
            my_dict[stones[i]] = i
        self.dp = [[None] * 2001 for _ in range(2001)]
        return self.traverse(0, 0, my_dict, stones)
    def traverse(self, jumps, curr_idx, my_dict, stones):
        if curr_idx == len(stones) - 1:
            return True
        if self.dp[jumps][curr_idx] != None:
            return self.dp[jumps][curr_idx]
        hop1 = False 
        hop2 = False
        hop3 = False 
        case1 = stones[curr_idx] + jumps
        case2 = stones[curr_idx] + jumps + 1
        case3 = stones[curr_idx] + jumps - 1
        if jumps == 0:
            if case2 in my_dict:
                self.dp[jumps][curr_idx] = self.traverse(jumps + 1, my_dict[case2], my_dict, stones)
                return self.dp[jumps][curr_idx]
            else:
                self.dp[jumps][curr_idx] = False
                return False
        if case1 in my_dict :
            hop1 = self.traverse(jumps, my_dict[case1], my_dict, stones)
        if case2 in my_dict :
            hop2 = self.traverse(jumps + 1, my_dict[case2], my_dict, stones)
        if case3 in my_dict and jumps != 1:
            hop3 = self.traverse(jumps - 1, my_dict[case3], my_dict, stones)
        self.dp[jumps][curr_idx] = hop1 or hop2 or hop3 
        return self.dp[jumps][curr_idx]