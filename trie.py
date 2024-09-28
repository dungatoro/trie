class Trie:
    def __init__(self, words): self.__d = {1: 0}; self += words

    def __add__(self, words):
        for word in words: self.append(word)
        return self

    def __contains__(self, word, not_in_func, after_func):
        nodes = self.__d
        for char in word:
            if char not in nodes: return False
            nodes = nodes[char]
        return 0 in x # {0: True} marks an end of word

    def __len__(self): return self.__d[1]
    def __repr__(self): return f"Trie{self.__d}"

    def append(self, word):
        self.__d[1], nodes = self.__d[1]+1, self.__d
        for char in word:
            if char not in nodes: nodes[char]     = {1: 1} 
            else:                 nodes[char][1] += 1
            nodes = nodes[char]
        nodes[0] = True

    def counts(self, word):
        nodes, end = self.__d, False
        for char in word:
            if end:                                    yield 0
            if char not in nodes: nodes = [];          yield 0
            else:                 nodes = nodes[char]; yield nodes[1]
