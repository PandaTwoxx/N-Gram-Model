from service.train import train
from service.predict import predict
from joblib import load

import os

def run():
    first_try = True
    token_count = 10000
    while True:
        if first_try:
            print('Hello, please enter password')
        else:
            print('Incorrect password, try again')
        password = input('Password:')
        if password == 'password':
            break
        first_try = False
    while True:
        command = input('Enter command, enter help for more info:')
        if command == 'help':
            print('Enter train to train a model')
            print('Enter lm to view model list')
            print('Enter predict to run a prediction')
            print('Enter token to enter maximum prediction length (default 10000)')
            print('Enter exit to abort')
        if command == 'token':
            token_count = input('Enter new token amount:')
        if command == 'lm':
            with os.scandir('models/') as entries:
                for entry in entries:
                    if entry.is_file():
                        print(entry.name)
        if command == 'train':
            name = input('Enter new model name (We suggest that it ends with .joblib)')
            input('Press enter to train (Put training data in service/data/files, put file names in service/data/directory.txt):')
            print('Now training, if certain used training data is not up to data, re-launch the application')
            train(name)
            print('Training completed')
        if command == 'predict':
            model_name = input('Enter model name:')
            prompt = input('Enter prompt:')
            output = ''
            model = load('models/'+model_name)
            try:
                output = predict(prompt, model, token_count)
            except ValueError as e:
                print(e)
            print(output)
        if command == 'exit':
            break