class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth >= (cost1 + cost2) :
            return (need1 * cost1) + (need2 * cost2)
        if need1 > need2 :
            need1, need2, cost1, cost2 = need2, need1, cost2, cost1
        ans = costBoth * need1
        diff = need2 - need1
        if costBoth < cost2 :
            ans += (costBoth * diff)
        else:
            ans += (cost2 * diff)
        return ans