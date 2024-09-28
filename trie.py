class Trie:
    """ 
    The trie is represented via nested dictionaries, each character is a key to
    a dictionary of the characters that can follow it, which this pattern 
    repeating.

    As only characters are used, other datatypes can store extra info. 
     - 0 distinguishes the end of a word
     - 1 stores a count 
    """
    dictionary = {}

    def __init__(self, strings):
        """ Initialise from list of strings """
        for string in strings:
            children = self.dictionary # start at first layer of tree
            for letter in string:
                if letter not in children: 
                    children[letter] = {} # `letter` becomes a child node
                children = children[letter] # traverse to next layer
            children[0] = 0 # use to store end of a word

    def __contains__(self, string):
        """ Return whether word is `in` the tree """
        children = self.dictionary
        for letter in string:
            if letter not in children: return False
            children = children[letter]
        return 0 in children

    def __call__(self, string):
        self.__search_string = string
        return self

    def __iter__(self):
        """ Iterates over a string and returns the entire tree below """
        children = self.dictionary 
        for letter in self.__search_string:
            if letter not in children:
                yield None
            else:
                children = children[letter]
                yield self.__from_dict(children)

    def append(self, string):
        """ Add a single string to the trie """
        children = self.dictionary 
        for letter in string:
            if letter not in children: 
                children[letter] = {}
            children = children[letter]
        children[0] = 0

    def __add__(self, strings):
        for string in strings:
            self.append(string)
        return self

    def __from_dict(self, dictionary):
        trie = Trie([])
        trie.dictionary = dictionary
        return trie

    def suffixes(self, string):
        """ Find child nodes (suffixes) of a string """
        children = self.dictionary
        for letter in string:
            if letter not in string: return None
            children = children[letter]

        return self.__from_dict(children) # convert to trie to keep methods

    def __repr__(self):
        return f"Trie{self.dictionary}"

trie = Trie(["cat", "cot", "comb", "combs", "dog", "dogs"])
