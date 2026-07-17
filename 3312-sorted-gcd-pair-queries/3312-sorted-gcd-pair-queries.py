class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        mp = [0] * (mx + 1)
        for x in nums:
            mp[x] += 1

        cnt = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            curr = 0
            for k in range(i, mx + 1, i):
                curr += mp[k]
            cnt[i] = curr * (curr - 1) // 2
            for k in range(2 * i, mx + 1, i):
                cnt[i] -= cnt[k]

        for i in range(1, mx + 1):
            cnt[i] += cnt[i - 1]

        sol = []
        for q in queries:
            sol.append(bisect.bisect_left(cnt, q + 1))

        return sol