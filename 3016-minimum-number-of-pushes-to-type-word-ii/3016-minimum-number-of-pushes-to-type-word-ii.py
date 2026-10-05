class Solution:
    def minimumPushes(self, word: str) -> int:
        my_dict = {}
        for char in word :
            if char in my_dict :
                my_dict[char] += 1
            else :
                my_dict[char] = 1
        char_freq = []
        for key in my_dict :
            char_freq.append([key, my_dict[key]])
        def custom_sort(x):
            return -x[1]
        char_freq.sort(key=custom_sort)
        print(char_freq)
        ans = 0
        button_count = 1
        curr_place = 1 #curr_place is gonna get updated
        for i in range(len(char_freq)):
            _, freq = char_freq[i]
            ans += (button_count * freq)
            curr_place += 1
            if curr_place > 8 :
                curr_place = 1 
                button_count += 1
        return ans