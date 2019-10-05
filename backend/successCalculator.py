import random
import sys

trials = 100000

def estimateSuccessWithMonteCarlo_2Channel(row :int):
    letters = 'ACTG'
    success = 0
    for i in range(trials):
        word = ''.join(random.choice(letters) for i in range(row))
        if word.__contains__('A') or (word.__contains__('C') and word.__contains__('T')):
            success += 1
    return float(success)/trials

def estimateSuccessWithMonteCarlo_4Channel(row :int):
    letters = 'ACTG'
    success = 0
    for i in range(trials):
        word = ''.join(random.choice(letters) for i in range(row))
        if word.__contains__('A') and word.__contains__('C') and word.__contains__('T') and word.__contains__('G'):
            success += 1
    return float(success)/trials

def estimateSuccessWithMonteCarlo_2ChannelAlt(row :int, column :int):
    letters = 'ACTG'
    success = 0
    for i in range(trials):
        for j in range(column):
            word = ''.join(random.choice(letters) for i in range(row))
            if not(word.__contains__('A') or (word.__contains__('C') and word.__contains__('T'))):
                success -= 1
                break    
        success += 1
    return float(success)/trials


if __name__ == "__main__":
    channel = sys.argv[1]
    if channel == "2":
        p = estimateSuccessWithMonteCarlo_2Channel(int(sys.argv[3]))
    else:
        p = estimateSuccessWithMonteCarlo_4Channel(int(sys.argv[3]))
    print(p, end=" ")
    r = pow(p, int(sys.argv[2]))
    print(r, end=" ")
    q = pow(r , int(sys.argv[4]))
    print(q)
        
        