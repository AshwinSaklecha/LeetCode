class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        my_set = set()
        custom_words = ["A", "C", "G", "T"]
        visited = set()
        for word in bank:
            my_set.add(word)
        qu = deque()
        qu.append((startGene, 0))
        visited.add(startGene)
        while qu:
            word, level = qu.popleft()
            if word == endGene:
                return level
            for i in range(len(custom_words)):
                for j in range(len(word)):
                    new_word = word[:j] + custom_words[i] + word[j+1:]
                    if new_word not in visited and new_word in my_set:
                        visited.add(new_word)
                        qu.append((new_word, level + 1))
        return -1