class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        self.dp = [[None] * len(words[0]) for _ in range(len(target))]
        my_list = [{} for _ in range(len(words[0]))]
        for j in range(len(words[0])):
            for i in range(len(words)):
                my_dict = my_list[j]
                if words[i][j] in my_dict:
                    my_dict[words[i][j]] += 1
                else:
                    my_dict[words[i][j]] = 1
        # print(my_list)
        self.mod = int(1e9) + 7
        return self.traverse(0, 0, target, words, my_list)
    def traverse(self, i, j, target, words, my_list):
        if i >= len(target):
            return 1
        if j >= len(words[0]):
            return 0
        if self.dp[i][j] != None:
            return self.dp[i][j]
        ans = 0
        my_dict = my_list[j]
        if target[i] in my_dict:
            freq = my_dict[target[i]]
            ans = (freq * self.traverse(i+1, j+1, target, words, my_list)) % self.mod
        ans = (ans + self.traverse(i, j+1, target, words, my_list)) % self.mod
        self.dp[i][j] = ans
        return self.dp[i][j]