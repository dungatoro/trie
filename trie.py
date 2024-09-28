class Trie:
    def __init__(self, *words): self.nodes, self.count = {}, 1; self += words

    def append(self, word): 
        curr = self
        for i, letter in enumerate(word):
            if letter not in curr.nodes:
                curr.nodes[letter] = Trie(word[i+1:])
                return
            curr = curr.nodes[letter]; curr.count += 1
        curr.end = True

    def __add__(self, words):
        for word in words: self.append(word)
        return self

    def counts(self, word):
        curr, end = self, False
        for letter in word:
            if end == True: yield 0
            elif letter not in curr.nodes: end = True; yield 0
            else: curr = curr.nodes[letter]; yield curr.count
