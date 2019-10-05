import random

def estimateSuccessWithMonteCarlo(row :int, column :int):
    letters = 'ACTG'
    success = 0
    trials = 100000
    for i in range(trials):
        word = ''.join(random.choice(letters) for i in range(row))
        if word.__contains__('A') or (word.__contains__('C') and word.__contains__('T')):
            success += 1
    return pow(float(success)/trials, column)


def estimateSuccessWithMonteCarloAlt(row :int, column :int):
    letters = 'ACTG'
    success = 0
    trials = 100000
    for i in range(trials):
        for j in range(column):
            word = ''.join(random.choice(letters) for i in range(row))
            if not(word.__contains__('A') or (word.__contains__('C') and word.__contains__('T'))):
                success -= 1
                break    
        success += 1
    return float(success)/trials