import random

def estimateSuccessWithMonteCarlo(row :int, column :int):
    letters = 'ACTG'
    success = 0
    for i in range(1000):
        word = random.choice(letters)
        if word.__contains__('A') or (word.__contains__('C') and word.__contains__('T')):
            success += 1
    return pow(float(success)/1000,column)
