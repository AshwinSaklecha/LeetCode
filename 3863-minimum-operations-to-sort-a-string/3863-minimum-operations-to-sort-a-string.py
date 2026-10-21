class Solution:
    def minOperations(self, s: str) -> int:
        # observation, max answer can only be 3 
        if len(s) == 1 :
            return 0
        if len(s) == 2 :
            if s[0] > s[1] :
                return -1
            return 0
        
        my_dict = {}
        smallest = float('inf')
        biggest = float('-inf')

        for char in s :
            smallest = min(smallest, ord(char))
            biggest = max(biggest, ord(char))
            if ord(char) in my_dict :
                my_dict[ord(char)] += 1
            else :
                my_dict[ord(char)] = 1

        # todo : check if its completely increasing : complete
        flag = True #true means its increasing
        last_char = s[0]
        for i in range(1, len(s)):
            if ord(s[i]) >= ord(last_char):
                last_char = s[i]
            else:
                flag = False
                break
        if flag == True:
            return 0

        if ord(s[-1]) == biggest or ord(s[0]) == smallest :
            return 1
        if ord(s[-1]) == smallest and ord(s[0]) == biggest:
            if my_dict[biggest] > 1 or my_dict[smallest] > 1 :
                return 2 
            return 3
        if ord(s[-1]) == smallest :
            return 2
        return 2