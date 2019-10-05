import algorithm as alg

from algorithmChecker import checkAlgorithm

a = alg.BruteForce()
res = a.group()

for r in res:
    for s in r:
        print(s)
    print()

for r in res:
    if not checkAlgorithm(r):
        print("UPS! -> ", r)