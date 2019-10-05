import collections 

def readNgsFile(filename, header=None):
    with open(filename) as file:
        if header:
            file.readline()
        else:
            header = file.readline().replace("/","").strip().split(" ")
        resultDict = {x:[] for x in header if x}
        for line in file:
            for ind, val in enumerate(line.strip().split(" ")):
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
# print(createStructure(resultDataDict["i7"])[6<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>])