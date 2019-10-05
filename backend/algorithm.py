import algorithmChecker as ac


class Algorithm:

    def __init__(self, runs, samples, i7, i5=None):
        if i5 is None:
            self.indecies = [(i, ) for i in range(len(i7))]
        else:
            self.indecies = [(i, j) for i in range(len(i7)) for j in range(len(i5))]
        
        self.i7 = i7
        self.i5 = i5
        self.runs = runs
        self.samples = samples


    def _checkGroup(self, group):
        return None


    def group(self):
        return None


class BruteForce(Algorithm):

    def group(self):
        return self._bruteForce(self.indecies)

    
    def _checkGroup(self, group):
        converted = []

        for sample in group:
            txt = self.i7[sample[0]]
            if self.i5 is not None:
                txt += self.i5[sample[1]]
            converted.append(txt)

        # for c in converted:
        #     print(c)
        # print(ac.checkAlgorithm(converted))
        # print()
        
        return ac.checkAlgorithm(converted)
    

    def _bruteForce(self, left, groups=[]):
        # print("Left:", left)
        # print("Groups:", groups)
        # input("Press Enter to continue...")

        if len(left) == 0:
            return groups

        if len(groups) > 0:
            if len(groups[-1]) >= self.samples:
                if not self._checkGroup(groups[-1]):
                    return None
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


class BruteForceFour(BruteForce):
    
    def _checkGroup(self, group):
        return None

        # TODO: return ac.checkAlgorithm(group)
