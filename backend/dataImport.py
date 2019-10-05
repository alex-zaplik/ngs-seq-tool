import collections 

def readNgsFile(filename, indexes):
    result = []
    with open(filename) as file:
        header = file.readline().replace("/","").strip().split(" ")
        if not all(x in range(1, len(header)) for x in indexes):
            raise Exception
        for line in file:
            lineList = line.strip().split(" ")
            resultDict = {header[x]:lineList[x] for x in indexes}
            resultNamedTuple = collections.namedtuple(lineList[0], resultDict.keys())(**resultDict)
            result.append(resultNamedTuple)
        return result
        

def createStructure(resultList, column):
    resDict = {}
    for position in range(len(resultList[0][column])):
        print(len(resultList[0][0]))
        resDict[position] = {}
        for code in ['C', 'A', 'T', 'G']:
            resDict[position][code] = []
            for ind, val in enumerate(resultList):
                if val[column][position] == code:
                    resDict[position][code].append(ind)
    return resDict

def createStructureFromFile(filename, column):
    file = readNgsFile(filename, [column])
    return createStructure(file, 0)

result = createStructureFromFile("backend/data/indexy_illumina.txt", 3)
print(result[2]["C"])