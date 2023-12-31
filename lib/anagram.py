class Anagram():
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, anagrams):
        return [anagram for anagram in anagrams if sorted(anagram.lower()) == self.sorted_word and anagram.lower() != self.word]