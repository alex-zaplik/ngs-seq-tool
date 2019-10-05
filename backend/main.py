import algorithm as alg
import argparse
import customGenerator as cg

from algorithmChecker import checkAlgorithm
from dataImport import readNgsFile


parser = argparse.ArgumentParser()

parser.add_argument('--path', type=str, help="Path to the data file")
parser.add_argument('--indexing', type=str, choices=("single", "double"), help="Indexing method. Expectig 'i7' if 'single' and 'i7' as well as 'i5' if 'double'")
parser.add_argument('--runs', type=int, help="The number of sequencing runs")
parser.add_argument('--samples', type=int, help="The number of DNA samples per run")
parser.add_argument('--i7', type=int, help="Column index for i7 indecies")
parser.add_argument('--i5', type=int, help="Column index for i5 indecies (ignored if indexing is set to 'single')")

args = parser.parse_args()


# columns = (args['i7'], args['i5']) if args['indexing'] == 'double' else (args['i7'])
# print(readNgsFile("data/indexy_illumina.txt", columns))


# i7 = cg.generateCorrectSequences(1, 4, 10)
# i5 = cg.generateCorrectSequences(1, 4, 10)

# a = alg.BruteForce(args['runs'], args['samples'], i7, i5=i5)
# res = a.group()
# for r in res:
#     for s in r:
#         print(s)
#     print()
