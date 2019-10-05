def readNgsFile(filename, indexes):
    result = []
    with open(filename) as file:
        for line in file:
            lineList = line.strip().split(" ")
            result.append(''.join([lineList[x] for x in indexes]))
    print(result)

