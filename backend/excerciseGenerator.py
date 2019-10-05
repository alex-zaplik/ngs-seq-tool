from customGenerator import generateCorrectSequences

import argparse
import sys

# liczba grup, liczba sampli, dlugosc sampli
generated = generateCorrectSequences(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

print("Label i5_index:")

for i, gen in enumerate(generated):
    print("X%03d %s" % (i, gen))
