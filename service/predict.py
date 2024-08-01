from service.classes import Model

def predict(prompt: str, model: Model):
    output = prompt + ' '
    words = prompt.split()
    if len(words) < 2:
        raise ValueError("Input string must contain at least two words.")
    word1 = words[-2]
    word2 = words[-1]
    for i in range(10000):
        word = model.predict(word1, word2)
        word1 = word2
        word2 = word
        output = output + word
        if not(word.endswith('.')):
            output = output + ' '
        else:
            break
    return output
