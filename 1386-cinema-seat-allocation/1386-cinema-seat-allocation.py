class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        last_seat = [1, 1]
        ans = 0
        
        # print(reservedSeats)
        for i in range(len(reservedSeats)):
            curr_seat = reservedSeats[i]
            if curr_seat[0] == last_seat[0]:
                if curr_seat[1] <= 5 or last_seat[1] >= 6 or (last_seat[1] == 2 and curr_seat[1] == 7) or (last_seat[1] == 4 and curr_seat[1] == 9):
                    ans += 0
                else:
                    ans += ((curr_seat[1] - last_seat[1]-1) // 4)
            else:

                # first free the last_seat
                if last_seat[1] <= 1:
                    ans += 2
                elif last_seat[1] <= 5 :
                    ans += 1

                # handle mid seats 
                remaining_rows = curr_seat[0] - last_seat[0] - 1 
                ans += (2 * (remaining_rows))

                # handle the curr_seat 
                if curr_seat[1] <= 5 :
                    ans += 0
                elif curr_seat[1] <= 9:
                    ans += 1
                else:
                    ans += 2

            last_seat = curr_seat

        if last_seat[1] <= 1:
            ans += 2
        elif last_seat[1] <= 5 :
            ans += 1
        remaining_rows = n - last_seat[0]
        ans += (2 * (remaining_rows))
        return ans