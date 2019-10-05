import collections 

def readNgsFile(filename, indexes):
    result = []
    with open(filename) as file:
        header = file.readline().strip().split(" ")
        for line in file:
            lineList = line.strip().split(" ")
            resultDict = {header[x]:lineList[x] for x in indexes}
            result.append(collections.namedtuple('Result', resultDict.keys())(**resultDict))
    print(result)

readNgsFile("backend/data/indexy_illumina.txt", [2,3])