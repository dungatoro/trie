class Trie:
    """ 
    The trie is represented via nested dictionaries, each character is a key to
    a dictionary of the characters that can follow it, which this pattern 
    repeating.

    As only characters are used, other datatypes can store extra info. 
    """
    __dict = {}

    def __init__(self, strings=None):
        """ Initialise from list of strings """
        if strings: 
            self += strings

    def __contains__(self, string):
        """ Return whether word is `in` the tree """
        children = self.__dict
        for letter in string:
            if letter not in children: 
                return False
            children = children[letter]
        return "end" in children

    def __call__(self, string):
        self.__search_string = string
        return self

    def __iter__(self):
        """ Iterates over a string and returns the entire tree below """
        children = self.__dict 
        for letter in self.__search_string:
            if letter not in children:
                yield None
            else:
                children = children[letter]
                yield self.__from_dict(children)

    def append(self, string):
        """ Add a single string to the trie """
        children = self.__dict # start at first layer of tree
        for letter in string:
            if letter not in children: 
                children[letter] = {"counts": 1} # `letter` becomes a child node
            else:
                children[letter]["counts"] += 1 # update count

            children = children[letter] # traverse to next layer
        children["end"] = True # use to store end of a word

    def __add__(self, strings):
        for string in strings:
            self.append(string)
        return self

    def __from_dict(self, dictionary):
        trie = Trie([])
        trie.__dict = dictionary
        return trie

    def suffixes(self, string):
        """ Find child nodes (suffixes) of a string """
        children = self.__dict
        for letter in string:
            if letter not in children: 
                return None
            children = children[letter]

        return self.__from_dict(children) # convert to trie to keep methods

    def __repr__(self):
        return f"Trie{self.__dict}"

    def __len__(self):
        return self.__dict.get("counts") or len(self.__dict) 

trie = Trie()
l = ["cat", "car", "cot", "comb", "combs", "dog", "dogs"]
trie = Trie(l)

for children in trie("cat"):
    print( len(children))
