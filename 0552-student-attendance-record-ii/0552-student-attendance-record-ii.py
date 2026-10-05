class Solution:
    def checkRecord(self, n: int) -> int:
        self.mod = int(1e9 + 7)
        self.dp = {}
        ans = self.traverse(n, 0, 0)
        return ans
    
    def traverse(self, days, absent, late):
        if absent >= 2 or late >= 3 :
            return 0
        if days == 0 :
            return 1
        if (days, absent, late) in self.dp :
            return self.dp[(days, absent, late)]
        path1 = self.traverse(days-1, absent + 1, 0)
        path2 = self.traverse(days-1, absent, late + 1)
        path3 = self.traverse(days-1, absent, 0)

        self.dp[(days, absent, late)] = (path1 + path2 + path3) % self.mod
        return self.dp[(days, absent, late)]