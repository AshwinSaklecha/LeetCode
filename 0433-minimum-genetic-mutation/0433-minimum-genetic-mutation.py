class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        my_set = set()
        custom_words = ["A", "C", "G", "T"]
        visited = set()
        for word in bank:
            my_set.add(word)
        ans = self.traverse(startGene, endGene, my_set, custom_words, visited)
        return -1 if ans == float('inf') else ans
    def traverse(self, curr_word, final_word, my_set, custom_words, visited):
        if curr_word == final_word:
            return 0
        steps = float('inf')
        for i in range(len(curr_word)):
            for j in range(len(custom_words)):
                each_step = float('inf')
                if custom_words[j] == curr_word[i]:
                    continue
                new_word = curr_word[:i] + custom_words[j] + curr_word[i+1:]
                if new_word in my_set and new_word not in visited:
                    visited.add(new_word)
                    each_step = 1 + self.traverse(new_word, final_word, my_set, custom_words, visited)
                    visited.remove(new_word)
                steps = min(steps, each_step)
        return steps