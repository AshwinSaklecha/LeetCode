class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [0] * len(words)
        prev_idx = [None] * len(words)
        max_val = 0 
        max_idx = -1
        for i in range(len(words)):
            for j in range(i):
                if self.is_ham_group(j, i, words, groups):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev_idx[i] = j

                        if dp[i] > max_val :
                            max_val = dp[i]
                            max_idx = i
        ans = []
        while max_idx != None :
            ans.append(words[max_idx])
            max_idx = prev_idx[max_idx]
        ans.reverse()
        return ans
    def is_ham_group(self, prev_i, i, words, groups):
        if len(words[i]) != len(words[prev_i]) or groups[i] == groups[prev_i]:
            return False
        hams = 0
        for idx in range(len(words[i])):
            if words[i][idx] != words[prev_i][idx]:
                hams += 1
        return hams == 1