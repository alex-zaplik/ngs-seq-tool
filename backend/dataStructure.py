def createDataStructure(resultList):
    resDict = {}
    for position in range(len(resultList[0])):
        resDict[position] = {}
        for code in ['C', 'A', 'T', 'G']:
            resDict[position][code] = []
            for x in resultList:
                if x[position] == code:
                    resDict[position][code].append(x)
    return resDict

