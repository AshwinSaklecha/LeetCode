class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        if len(coins) == 1 :
            return coins[0] * k
        coins.sort()
        start = coins[0]
        end = coins[-1] * k
        k -= 1
        while start <= end:
            mid = (start + end) // 2 
            elements_before_mid = self.calculate(mid, coins)
            if elements_before_mid == k :
                if self.divisible(mid, coins):
                    return mid
                start = mid + 1 
            elif elements_before_mid < k :
                start = mid + 1 
            else:
                end = mid - 1 

        return 69
    
    def divisible(self, num, coins):
        for i in range(len(coins)):
            if num % coins[i] == 0:
                return True
        return False

    def calculate(self, num, coins):
        total_numbers_before_num = 0
        
        # TODO : calculations to remove the duplicates, totally new approach!!!!
        # implement inclusion and exclusion and bitmask iteration 

        for i in range(1, 2 ** len(coins)):
            curr_lcm = -1 
            count_of_bits = 0
            for j in range(16): # because coins max length is 15 
                if i & (1 << j) != 0: # this bit has one 
                    count_of_bits += 1
                    if curr_lcm == -1 :
                        curr_lcm = coins[j]
                    else:
                        curr_lcm = math.lcm(curr_lcm, coins[j])
            if count_of_bits % 2 != 0:
                total_numbers_before_num += ((num - 1) // curr_lcm)

            else:
                total_numbers_before_num -= ((num - 1) // curr_lcm)

        return total_numbers_before_num