class Solution:
    def waysToReachStair(self, k: int) -> int:
        jump_power = [1]
        for i in range(1, 32):
            jump_power.append(jump_power[-1] * 2)
        self.dp = {}
        ans = self.traverse(1, 0, True, k, jump_power)
        return ans
    
    def traverse(self, step, jumps, can_go_down, target, jump_power):
        if step >= target + 2 :
            return 0
        key_str = str(step)+str(jumps)+str(can_go_down)
        if key_str in self.dp :
            return self.dp[key_str]
        path1 = self.traverse(step + jump_power[jumps], jumps + 1, True, target, jump_power)
        path2 = 0 
        if can_go_down :
            path2 = self.traverse(step - 1, jumps, False, target, jump_power)
        if step == target :
            path1 += 1
        self.dp[key_str] = path1 + path2
        return self.dp[key_str]