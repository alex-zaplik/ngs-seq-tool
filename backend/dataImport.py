import collections 

def readNgsFile(filename, indexes):
    result = []
    with open(filename) as file:
        header = file.readline().replace("/","").strip().split(" ")
        for line in file:
            lineList = line.strip().split(" ")
            resultDict = {header[x]:lineList[x] for x in indexes}
            result.append(collections.namedtuple('Result', resultDict.keys())(**resultDict))
    return result

print(readNgsFile("backend/data/indexy_illumina.txt", [0,1,2,3,4])[0])