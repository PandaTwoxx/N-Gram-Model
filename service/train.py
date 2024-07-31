from classes import Model, Data

from joblib import dump

def find(a, n: Data):
    for i in range(len(a)):
        if a[i].word1 == n.word1 and a[i].word2 == n.word2 and a[i].output == n.output:
            return i
    return None

def train():
    words = [str]
    files = [str]
    buffer = ''
    stuf = ''
    model = Model()
    print('Fetching data directories.')
    with open('service/data/directory.txt', 'r') as file:
        stuf = file.read()
        for j in range(len(stuf)):
            if stuf[j] == ' ' or stuf[j] == ';':
                files.append(buffer)
                buffer = ''
            else:
                buffer = buffer + stuf[j]
        file.close()
    print("Creating model...")
    for i in range(1, len(files)):
        with open(f'service/data/files/{files[i]}', 'r') as file:
            stuf = file.read()
            for j in range(len(stuf)):  
                if stuf[j] == ' ':
                    words.append(buffer)
                    buffer = ''
                elif stuf[j] == ';':
                    for i in range(0, len(words)-2):
                        dat = Data(words[i], words[i+1], words[i+2])
                        if find(model.dataset, dat) is not None:
                            model.dataset[find(model.dataset, dat)].add()
                        else:
                            model.dataset.append(dat)
                    words = []
                    buffer = ''
                else:
                    buffer = buffer + stuf[j]
            file.close()
    print('Model created')
    print('Saving model...')
    dump(model, 'model.joblib')
    print('Model saved')
train()