class Solution:
    def minimumPushes(self, word: str) -> int:
        my_dict = {}
        for char in word:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        char_freq = []
        for key in my_dict:
            char_freq.append([key, my_dict[key]])
        def custom_sort(x):
            return -x[1]
        char_freq.sort(key=custom_sort)
        print(char_freq)
        ans = 0
        for i in range(len(char_freq)):
            pushes = (i // 8) + 1
            ans += char_freq[i][1] * pushes

        return ans