import random
from algorithmChecker import checkAlgorithm


def generateSequences(samples: int, length: int):
    # random sequences
    letters = 'ATGC'
    better_letters = 'ATC'
    s = []
    for i in range(samples):
        temp = ''
        for j in range(length):
            if temp == '' or temp[-1] != 'G':
                temp += random.choice(letters)
            else:
                temp += random.choice(better_letters)
        s.append(temp)
    return s


def generateCorrectSequences(groups: int, samples: int, length: int):
    # correct sequences
    # powtórz względem ilości grup
    assert samples >= 2
    result = []
    for i in range(groups):
        # wygeneruj sample -1 losowo
        rows = generateSequences(samples - 1, length)
        # sprawdz czekerem gdzie jest False
        checker = checkAlgorithm(rows, True)
        # losuj slowo
        last_row = generateSequences(1, length)[0]
        # na false zamień na 'A'
        for j in range(length):
            if not checker[j]:
                s = ''.join(r[j] for r in rows) 
                if s.__contains__('T'):
                    letter = 'C'
                elif s.__contains__('C'):
                    letter = 'T'
                else:
                    letter = 'A'
                last_row = last_row[:j] + letter + last_row[min(j+1,length):]
        rows += [last_row]
        result += rows
    # przelosuj kolejność
    random.shuffle(result)
    return result