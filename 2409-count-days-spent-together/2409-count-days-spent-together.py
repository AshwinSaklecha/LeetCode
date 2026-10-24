class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_start = self.helper(arriveAlice)
        alice_end = self.helper(leaveAlice)
        bob_start = self.helper(arriveBob)
        bob_end = self.helper(leaveBob)

        if alice_start > bob_start :
            alice_start, alice_end, bob_start, bob_end = bob_start, bob_end, alice_start, alice_end
        
        if bob_start > alice_end :
            return 0
        
        start_day = max(alice_start, bob_start)
        end_day = min(alice_end, bob_end)

        return end_day - start_day + 1

    
    def helper(self, s):
        # s is date
        month = 0
        days = 0
        for i in range(2):
            month = (month * 10) + int(s[i])
        for i in range(3, len(s)):
            days = (days * 10) + int(s[i])
        total_days = 0
        for i in range(0, month-1):
            idx = i
            if i >= 7 :
                idx += 1
            if idx % 2 == 0 :
                total_days += 31
            elif idx == 1 :
                total_days += 28
            else :
                total_days += 30
        
        return total_days + days