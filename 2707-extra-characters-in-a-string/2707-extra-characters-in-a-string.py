class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        my_set = set()
        for word in dictionary:
            my_set.add(word)
        # current code Time complexity -> n * (2 ^ (n * n))
        # optimized code TC -> n * (n * n)
        self.dp = [[None] * len(s) for _ in range(len(s))]
        return self.traverse(0, 0, s, my_set)
    def traverse(self, i, j, s, my_set):
        if j >= len(s):
            if i >= len(s):
                return 0
            return j - i
        if self.dp[i][j] != None:
            return self.dp[i][j]
        path1 = self.traverse(i, j+1, s, my_set)
        path2 = None
        if s[i:j+1] in my_set:
            path2 = self.traverse(j+1, j+1, s, my_set)
        else:
            path2 = (j-i+1) + self.traverse(j+1, j+1, s, my_set)
        self.dp[i][j] = min(path1, path2)
        return self.dp[i][j]