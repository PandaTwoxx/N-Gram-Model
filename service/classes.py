import random

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
    dataset = []
    def predict(self, a, b) -> str:
        options = []
        for i in self.dataset:
            if i.word1 == a and i.word2 == b:
                for i in range(i.probability):
                    options.append(i)
        if len(options) == 0:
            raise ValueError("Couldn't find prompt in dataset")
        rand = random.randint(0,len(options)-1)
        return options[rand]