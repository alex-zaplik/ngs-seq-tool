import algorithm as alg
import argparse
import customGenerator as cg

from algorithmChecker import checkAlgorithm


parser = argparse.ArgumentParser()

parser.add_argument('--path', type=str, help="Path to the data file")
parser.add_argument('--indexing', type=str, choices=("single", "double"), help="Indexing method. Expectig 'i7' if 'single' and 'i7' as well as 'i5' if 'double'")

args = parser.parse_args()


runs = 6
samples = 4

i7 = cg.generateSequences(6 * 4, 10)

a = alg.BruteForce(6, 4, i7)
res = a.group()
for r in res:
    for s in r:
        print(s)
    print()

# i7 = cg.generateSequences(6, 10)
# i5 = cg.generateSequences(4, 10)

# a = alg.BruteForce(6, 4, i7, i5=i5)
# res = a.group()
# for r in res:
#     for s in r:
#         print(s)
#     print()

# for r in res:
#     if not checkAlgorithm(r):
#         print("UPS! -> ", r)