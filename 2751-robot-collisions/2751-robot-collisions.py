class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        positions_dict = {}
        phd = [] #positions, health, directions
        for i in range(len(positions)):
            positions_dict[positions[i]] = i
            phd.append([positions[i], healths[i], directions[i]])
        phd.sort()
        
        stack = []
        for chunk in phd:
            p, h, d = chunk 
            if d == "L":
                while stack and stack[-1][2] == "R" and h > 0:
                    if h == stack[-1][1]:
                        stack.pop()
                        h = 0
                        break
                    elif h > stack[-1][1] :
                        h -= 1
                        stack.pop()
                    elif h < stack[-1][1] :
                        stack[-1][1] -= 1
                        h = 0
                        break
                if h > 0 :
                    stack.append([p, h, d])
            else :
                stack.append(chunk)
        

        temp_ans = [-1] * len(positions)
        for chunk in stack :
            p, h, d = chunk 
            idx = positions_dict[p]
            temp_ans[idx] = h
        ans = []
        for num in temp_ans :
            if num != -1 :
                ans.append(num)
        return ans
        