class Solution:
    def minimumTotalDistance(self, robot: List[int], limit_factory: List[List[int]]) -> int:
        robot.sort()
        limit_factory.sort()
        factory = []
        for i in range(len(limit_factory)):
            location, limit = limit_factory[i]
            if limit == 0:
                continue
            for j in range(limit):
                factory.append(location)
        self.dp = [[None] * len(factory) for _ in range(len(robot))]
        ans = self.traverse(0, 0, robot, factory)
        return -1 if ans == float('inf') else ans
    def traverse(self, i, j, robot, factory):
        if i >= len(robot):
            return 0
        if j >= len(factory):
            return float('inf')
        if self.dp[i][j] != None:
            return self.dp[i][j]
        path1 = abs(robot[i] - factory[j]) + self.traverse(i+1, j+1, robot, factory)
        path2 = self.traverse(i, j+1, robot, factory)
        self.dp[i][j] = min(path1, path2)
        return self.dp[i][j]