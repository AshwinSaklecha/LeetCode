class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        self.dp = {}
        ans = self.traverse(0, books[0][-1], books[0][0], books, shelfWidth) 
        return ans
    
    def traverse(self, idx, max_height, curr_shelf, books, shelfWidth):
        if curr_shelf > shelfWidth:
            return float('inf')
        key_str = str(idx)+ "_" + str(max_height) + "_" + str(curr_shelf)
        if key_str in self.dp :
            return self.dp[key_str]
        path1 = max_height
        path2 = float('inf')
        if idx + 1 < len(books):
            path1 += self.traverse(idx+1, books[idx+1][-1], books[idx+1][0], books, shelfWidth)
            path2 = self.traverse(idx+1, max(max_height, books[idx+1][-1]), curr_shelf + books[idx+1][0], books, shelfWidth)
        
        self.dp[key_str] = min(path1, path2)
        return self.dp[key_str]