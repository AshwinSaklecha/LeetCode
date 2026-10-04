class Solution:
    def countSubstrings(self, s: str) -> int:
        is_pal = [[None] * len(s) for _ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                is_pal[i][j] = self.check(i, j, is_pal, s)
                if is_pal[i][j] :
                    ans += 1
        
        return ans
    
    def check(self, i, j, is_pal, s):
        if i == j :
            is_pal[i][j] = True
            return True
        if j == i + 1 :
            is_pal[i][j] = s[i] == s[j]
            return s[i] == s[j]
        if is_pal[i][j] != None :
            return is_pal[i][j]
        is_pal[i][j] = s[i] == s[j] and self.check(i+1, j-1, is_pal, s)
        return is_pal[i][j]
                        