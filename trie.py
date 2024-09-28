class Trie:
    def append(self, string):
        self.__dict["counts"] += 1
        children = self.__dict # start at first layer of tree
        for letter in string:
            if letter not in children: 
                children[letter] = {"counts": 1} # `letter` becomes a child node
            else:
                children[letter]["counts"] += 1 # update count

            children = children[letter] # traverse to next layer
        children["end"] = True # use to store end of a word

    def __add__(self, strings):
        for string in strings: self.append(string)
        return self

    def __init__(self, strings=None):
        self.__dict = {"counts": 0}
        if strings: self += strings

    def __from_dict(self, dictionary):
        trie = Trie([])
        trie.__dict = dictionary
        return trie

    def layer(self): return [key for key in self.__dict if len(key) == 1]
    def layers(self, string):
        children = self.__dict 
        for letter in string:
            if letter not in children:
                children = []
                yield None # yield None for the rest of the letters
            else:
                children = children[letter]
                yield self.__from_dict(children) # yield the letter's tree

    def __str_iter(self, string, not_in_func, after_func):
        children = self.__dict
        for letter in string:
            if letter not in children: 
                print(string, letter)
                return not_in_func(children) # return if letter not found
            children = children[letter]
        return after_func(children) # return after iteration

    def __contains__(self, string):
        return self.__str_iter(string, lambda x: False, lambda x: "end" in x)

    def suffixes(self, string):
        return self.__str_iter(string, lambda x: None, lambda x: self.__from_dict(x))

    def __len__(self): return self.__dict["counts"]
    def __repr__(self): return f"Trie{self.__dict}"
