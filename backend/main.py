import algorithm as alg
import argparse
import customGenerator as cg

from algorithmChecker import checkAlgorithm
from dataImport import readNgsFile, createStructure


SINGLE = "single"
DOUBLE = "double"

I7 = 'i7'
I5 = 'i5'
NAME = 'name'


parser = argparse.ArgumentParser()

parser.add_argument('--path', type=str, help="Path to the data file")
parser.add_argument('--indexing', type=str, choices=(SINGLE, DOUBLE), help="Indexing method. Expectig 'i7' if 'single' and 'i7' as well as 'i5' if 'double'")
parser.add_argument('--runs', type=int, help="The number of sequencing runs")
parser.add_argument('--samples', type=int, help="The number of DNA samples per run")
parser.add_argument('--i7', type=int, help="Column index for i7 indecies")
parser.add_argument('--i5', type=int, help="Column index for i5 indecies (ignored if indexing is set to 'single')")

args = parser.parse_args()


if args.indexing == DOUBLE:
    columns = [None for _ in range(max(args.i7, args.i5) + 1)]
    columns[0] = NAME
    columns[args.i7] = I7
    columns[args.i5] = I5
else:
    columns = [None for _ in range(args.i7 + 1)]
    columns[0] = NAME
    columns[args.i7] = I7

content = readNgsFile(args.path, columns)
i7 = createStructure(content[I7])
i5 = createStructure(content[I5]) if args.indexing == DOUBLE else None

optim = alg.OptimizedDouble(args.runs, args.samples, len(content[I7][0]), i7, i5=i5, i5_len=len(content[I5][0]) if I5 in content else 0)
res = optim.group()

if res is None:
    i7 = content[I7]
    i5 = content[I5] if args.indexing == DOUBLE else None

    a = alg.BruteForce(args.runs, args.samples, i7, i5=i5)
    res = a.group()

for r in res:
    for s in r:
        cols = [I7, I5]
        for index in range(len(s)):
            print(content[NAME][s[index]], content[cols[index]][s[index]], end=" ")
        print()
    print()
