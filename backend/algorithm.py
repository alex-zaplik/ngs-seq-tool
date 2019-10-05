import customGenerator as cg

class Algorithm:

    def __init__(self, indecies=None, runs=6, samples=4, length=8):
        if indecies is None:
            indecies = cg.generateSequences(runs * samples, length)

        self.indecies = indecies
        self.runs = runs
        self.samples = samples
    

    def _bruteForce(self, left, groups=[]):
        # print("Left:", left)
        # print("Groups:", groups)
        # input("Press Enter to continue...")

        if len(left) == 0:
            return groups

        if len(groups) > 0:
            if len(groups[-1]) >= self.samples:
                # TODO: Chech if groups[-1] is correct. If not: return None
                groups.append([])
        else:
            groups.append([])
        
        curr = groups[-1]
        res = None

        for i in range(len(left)):
            new_left = left[:]
            del new_left[i]
            new_groups = groups[:-1] + [curr + [left[i]]]
            res = self._bruteForce(new_left, new_groups)

            if res is not None:
                groups = new_groups
                break
        
        return res



    def bruteForce(self):
        return self._bruteForce(self.indecies)
