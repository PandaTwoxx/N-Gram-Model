class Data:
    word1 = ''
    word2 = ''
    output = ''
    probability = 0
    def __init__(self, word1, word2, output, probability = 1):
        self.word1 = word1
        self.word2 = word2
        self.output = output
        self.probability = probability
    def add(self):
        self.probability += 1

class Model:
    dataset = [Data]
