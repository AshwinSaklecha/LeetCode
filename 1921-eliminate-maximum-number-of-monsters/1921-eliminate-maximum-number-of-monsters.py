class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        time = []
        for i in range(len(dist)):
            time.append(dist[i]/speed[i])
        time.sort()
        print(time)

        time_taken = 0
        ans = 0 
        for t in time :
            if time_taken < t :
                ans += 1
                time_taken += 1
            else :
                break
        
        return ans

