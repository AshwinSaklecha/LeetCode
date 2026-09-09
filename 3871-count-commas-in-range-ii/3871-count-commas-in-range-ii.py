class Solution:
    def countCommas(self, n: int) -> int:
        # 1 - 999 => 0 comma (0 to [(10 ** 3) - 1])
        # 1,000 - 999,999 => 1 comma (10 ** 3 to [(10 ** 6) - 1])... and so on....
        # 1,000,000 - 999,999,999 => 2 commas 
        # 1,000,000,000 - 999,999,999,999 => 3 commas 
        # 1,000,000,000,000 - 999,999,999,999,999 => 4 commas 
        # 1,000,000,000,000,000 - 999,999,999,999,999,999 => 5 commas 

        ten_powers = [1]
        for i in range(20):
            ten_powers.append(10 * ten_powers[-1])
        ans = 0
        if n >= ten_powers[3]:
            lower_limit = ten_powers[3]
            upper_limit = min(ten_powers[6] - 1, n)
            ans += ((upper_limit - lower_limit) + 1)
        if n >= ten_powers[6]:
            lower_limit = ten_powers[6]
            upper_limit = min(ten_powers[9] - 1, n)
            ans += (((upper_limit - lower_limit) + 1) * 2 )
        if n >= ten_powers[9]:
            lower_limit = ten_powers[9]
            upper_limit = min(ten_powers[12] - 1, n)
            ans += (((upper_limit - lower_limit) + 1) * 3 )
        if n >= ten_powers[12]:
            lower_limit = ten_powers[12]
            upper_limit = min(ten_powers[15] - 1, n)
            ans += (((upper_limit - lower_limit) + 1) * 4 )
        if n >= ten_powers[15]:
            lower_limit = ten_powers[15]
            upper_limit = min(ten_powers[18] - 1, n)
            ans += (((upper_limit - lower_limit) + 1) * 5)
        
        return ans