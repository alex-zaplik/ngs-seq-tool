import algorithm as alg
import argparse

from algorithmChecker import checkAlgorithm


parser = argparse.ArgumentParser()

parser.add_argument('--path', type=str, help="Path to the data file")
parser.add_argument('--indexing', type=str, choices=("single", "double"), help="Indexing method. Expectig i7 if 'single' and 'i7' as well as 'i5' if 'double'")

args = parser.parse_args()


a = alg.BruteForce()
res = a.group()

for r in res:
    for s in r:
        print(s)
    print()

for r in res:
    if not checkAlgorithm(r):
        print("UPS! -> ", r)