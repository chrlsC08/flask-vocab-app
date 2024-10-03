class Vocabulary:
    def __init__(self):
        self.words = {}

    def add_word(self, word, meaning):
        self.words[word] = meaning

    def get_all_words(self):
        return self.words

    def get_word(self, word):
        return self.words.get(word)

    def update_word(self, word, new_meaning):
        if word in self.words:
            self.words[word] = new_meaning
            return True
        return False

    def delete_word(self, word):
        if word in self.words:
            del self.words[word]
            return True
        return False