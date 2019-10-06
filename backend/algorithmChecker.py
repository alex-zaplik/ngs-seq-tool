def checkAlgorithm(algorithmOutput, extraData= False):
    if not extraData:
        for column in range(len(algorithmOutput[0])):
            s = ''.join(row[column] for row in algorithmOutput)
            if not s.__contains__('A') and not (s.__contains__('C') and s.__contains__('T')):
                return False
        return True
    
    result = []
    for column in range(len(algorithmOutput[0])):
        s = ''.join(row[column] for row in algorithmOutput)
        if not s.__contains__('A') and not (s.__contains__('C') and s.__contains__('T')):
            result.append(False)
        else:
            result.append(True)
    return result


def checkAlgorithm_4Channel(algorithmOutput, extraData= False):
    if not extraData:
        for column in range(len(algorithmOutput[0])):
            s = ''.join(row[column] for row in algorithmOutput)
            if not (s.__contains__('A') and s.__contains__('C') and s.__contains__('T') and s.__contains__('G')):
                return False
        return True
    
    result = []
    for column in range(len(algorithmOutput[0])):
        s = ''.join(row[column] for row in algorithmOutput)
        if not (s.__contains__('A') and s.__contains__('C') and s.__contains__('T') and s.__contains__('G')):
            result.append(False)
        else:
            result.append(True)
    return result
