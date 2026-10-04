class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        my_dict = {}
        for num in arr :
            if num in my_dict :
                my_dict[num] += 1
            else :
                my_dict[num] = 1
        
        num_freq = []
        for key in my_dict:
            num_freq.append([key, my_dict[key]])
        def custom_sort(x):
            return x[1], x[0]
        num_freq.sort(key=custom_sort)
        print(num_freq)


        for i in range(len(num_freq)):
            num, freq = num_freq[i]
            if k >= freq :
                k -= freq
            else :
                return len(num_freq) - i
        return 0