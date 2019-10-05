import dataStructure
import dataImport

file = dataImport.readNgsFile("backend/data/indexy_illumina.txt", [0,1,2,3,4])[0]
print(file)
structure = dataStructure.createDataStructure(file)
print(structure)