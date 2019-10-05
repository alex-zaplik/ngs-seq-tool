import collections 
import re

def readNgsFile(filename, header=None):
    with open(filename) as file:
        if header:
            file.readline()
        else:
            clearLine = file.readline().strip().replace("/","")
            header = re.findall(r"[\w']+", clearLine)
        resultDict = {x:[] for x in header if x}
        for line in file:
            splitLine = re.findall(r"[\w']+", line)
            for ind, val in enumerate(splitLine):
                if ind >= len(header):
                    break
                if header[ind]:
                    resultDict[header[ind]].append(val)
        return resultDict
        

def createStructure(resultList):
    resDict = {}

    if any(len(resultList[0]) != len(x) for x in resultList):
        raise Exception

    for position in range(len(resultList[0])):
        resDict[position] = {}
        for code in ['C', 'A', 'T', 'G']:
            resDict[position][code] = []
            for ind, val in enumerate(resultList):
                if val[position] == code:
                    resDict[position][code].append(ind)
    return resDict

# resultDataDict = readNgsFile("backend/data/indexy_illumina.txt", ["name", None, "i7", None, "i5"])
# print(createStructure(resultDataDict["i7"]))