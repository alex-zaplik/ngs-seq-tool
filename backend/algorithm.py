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


class OptimizedDouble(DoubleChannel):
    def __init__(self, runs, samples, i7_len, i7, i5=None, i5_len=0):
        super().__init__(runs, samples, i7, i5)

        self.i7_len = i7_len
        self.i5_len = i5_len
    
    def _getBestElements(self, leftMostMin, index):
        if index < self.i7_len:
            structure = self.i7
        else:
            index -= self.i7_len
            structure = self.i5
        
        bestElements = structure[index]

        # TODO need to return where are indexes from, i7 or i5
        if leftMostMin == 0:
            if bestElements['A'] is not None:
                return bestElements['A']
            elif bestElements['C'] is not None:
                if bestElements['T'] is not None:
                    return bestElements['C'] + bestElements['T']
                else:
                    return bestElements['C']
            else:
                # no solution
                pass
        elif leftMostMin == 1:
            # take C
            if bestElements['C'] is not None:
                return bestElements['C']
            elif bestElements['A'] is not None:
                return bestElements['A']
            else:
                # no solution
                pass
        elif leftMostMin == 2:
            # take T
            if bestElements['T'] is not None:
                return bestElements['T']
            elif bestElements['A'] is not None:
                return bestElements['A']
            else:
                # no solution
                pass
        else:
            # take G
            if bestElements['G'] is not None:
                return bestElements['G']
            elif bestElements['C'] is not None:
                if bestElements['T'] is not None:
                    return bestElements['C'] + bestElements['T']
                else:
                    return bestElements['C']
            elif bestElements['A'] is not None:
                return bestElements['A']
            else:
                # no solution
                pass


    def _heuristic(self, left, groups=[]):
        
        # Initialize row scores
        row_scores = [0 for _ in range(self.i7_len + self.i5_len)]

        for i in range(self.samples):
            # Pick the leftmost minimum
            leftMostMin = min(row_scores)
            index = row_scores.index(leftMostMin)
            # maybe this fun only once? then scoring?
            print(self._getBestElements(leftMostMin, index))
            break

        return None