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
    

    def _heuristic(self, left, groups=[]):
        return None


    def _group(self, left, groups=[]):
        # print("Left:", left)
        # print("Groups:", groups)
        # input("Press Enter to continue...")

        if len(left) == 0:
            return groups

        if len(groups) > 0:
            if len(groups[-1]) >= self.samples:
                if not self._checkGroup(groups[-1]):
                    return None

                if len(groups) >= self.runs:
                    return groups

                groups.append([])
        else:
            groups.append([])
        
        return self._heuristic(left, groups)
    

    def group(self):
        return self._group(self.indecies)


class DoubleChannel(Algorithm):
    def _checkGroup(self, group):
        converted = []

        for sample in group:
            txt = self.i7[sample[0]]
            if self.i5 is not None:
                txt += self.i5[sample[1]]
            converted.append(txt)
        
        return ac.checkAlgorithm(converted)


class BruteForce(DoubleChannel):
    def _heuristic(self, left, groups=[]):
        curr = groups[-1]
        res = None

        for i in range(len(left)):
            new_left = left[:]
            del new_left[i]
            new_groups = groups[:-1] + [curr + [left[i]]]
            res = self._group(new_left, new_groups)

            if res is not None:
                groups = new_groups
                break
        
        return res

