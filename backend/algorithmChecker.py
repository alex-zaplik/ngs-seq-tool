def checkAlgorithm(algorithmOutput):
    for column in range(len(algorithmOutput[0])):
        s = ''.join(row[column] for row in algorithmOutput)
        if not s.__contains__('A') and not (s.__contains__('C') and s.__contains__('T')):
            return False
    return True