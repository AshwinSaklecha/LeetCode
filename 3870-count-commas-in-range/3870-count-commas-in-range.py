class Solution:
    def countCommas(self, n: int) -> int:
        # 1000 - 999,999 => 1 comma 
        if n < 1000:
            return 0
        
        return n - 1000 + 1