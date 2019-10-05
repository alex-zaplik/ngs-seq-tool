import random

def generateSequences(samples: int, length: int):
    letters = 'ATGC'
    s = []
    for i in range(samples):
        s.append(''.join(random.choice(letters) for j in range(length)))
    return s
