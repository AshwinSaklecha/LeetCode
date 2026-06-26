class Solution:
    def longestBalanced(self, s: str) -> int:
        # approach - take 2 dictionaries, one tracks the frequency of characters, another tracks the frequency of frequency 
        ans = 1
        for i in range(len(s)):
            char_freq = {}
            freq_freq = {}
            for j in range(i, len(s)):
                if s[j] in char_freq :
                    char_freq[s[j]] += 1
                else:
                    char_freq[s[j]] = 1
                curr_character_frequency = char_freq[s[j]]
                remove_frequency = curr_character_frequency - 1
                if curr_character_frequency in freq_freq :
                    freq_freq[curr_character_frequency] += 1
                else:
                    freq_freq[curr_character_frequency] = 1
                if remove_frequency in freq_freq:
                    freq_freq[remove_frequency] -= 1
                    if freq_freq[remove_frequency] == 0:
                        freq_freq.pop(remove_frequency)
                if len(freq_freq) == 1:
                    ans = max(ans, j - i + 1)
        return ans