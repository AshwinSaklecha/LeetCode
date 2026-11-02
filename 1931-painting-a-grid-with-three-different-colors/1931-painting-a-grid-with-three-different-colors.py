class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        self.mod = int(1e9) + 7
        self.dp = {}
        store = []
        rgb = ["R", "G", "B"]
        curr_store = []
        self.permute(0, "X", rgb, store, curr_store, m)
        print(store)

        ans = self.traverse(0, "", n, store)
        return ans
    
    def traverse(self, i, prev_color_line, n, store):
        if i >= n :
            return 1
        key_str = str(i) + "_" + str(prev_color_line)
        if key_str in self.dp:
            return self.dp[key_str]
        path = 0
        for color_line in store :
            if self.check(color_line, prev_color_line):
                path = (path + self.traverse(i+1, color_line, n, store)) % self.mod
        
        self.dp[key_str] = path
        return self.dp[key_str]
    
    def check(self, color1, color2):
        if len(color2) == 0 :
            return True
        
        for i in range(len(color1)):
            if color1[i] == color2[i]:
                return False
        return True
    
    def permute(self, i, prev_color, rgb, store, curr_store, max_len):
        if i == max_len:
            curr_store_str = "".join(curr_store)
            store.append(curr_store_str)
            return 
        for color in rgb :
            if prev_color != color :
                curr_store.append(color)
                self.permute(i+1, color, rgb, store, curr_store, max_len)
                curr_store.pop()