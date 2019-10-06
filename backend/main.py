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

#testowe polecenie (z backendu)
#python3 main.py --path "data/index_nextera.txt" --indexing "double" --runs 1 --samples 4 --i7 1 --i5 2

#testowe polecenie (z frontendu)
#python3 ../backend/main.py --path uploads/10:05:2019-08:14:09_indexy_vazyme.txt --indexing single --runs 4 --samples 4 --i7 1

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

optim = alg.OptimizedDouble(args.runs, args.samples, content, i7, i5=i5)
res = optim.group()

# res = None
if res is None:
    print("Dropping to BruteForce")
    i7 = content[I7]
    i5 = content[I5] if args.indexing == DOUBLE else None

    a = alg.BruteForce(args.runs, args.samples, content, i7, i5=i5)
    res = a.group()

if res is not None:
    for r in res:
        for s in r:
            cols = [I7, I5]
            for index in range(len(s)):
                print(content[NAME][s[index]], content[cols[index]][s[index]], end=" ")
            print()
        print()
else:
    # TODO: Error
    pass
