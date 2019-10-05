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


    def _new_group_extra(self):
        pass


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
                self._new_group_extra()
        else:
            groups.append([])
            self._new_group_extra()
        
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
    def __init__(self, runs, samples, content, i7, i5=None):
        super().__init__(runs, samples, i7, i5)

        self.i7_len = len(content['i7'][0])
        self.i5_len = len(content['i5'][0]) if 'i5' in content else 0
        self.content = content

    
    def _new_group_extra(self):
        self.row_scores = [0 for _ in range(self.i7_len + self.i5_len)]
    
    
    def _get_best_elements(self, leftMostMin, index, structure):    
        bestElements = structure[index]

        if leftMostMin == 0:
            # G or empty
            if bestElements['A'] is not None:
                bestElements = bestElements['A']
            elif bestElements['C'] is not None:
                if bestElements['T'] is not None:
                    bestElements = bestElements['C'] + bestElements['T']
                else:
                    bestElements = bestElements['C']
            elif bestElements['T'] is not None:
                bestElements = bestElements['T']
            else:
                # no solution
                return None
        elif leftMostMin == 1:
            # T
            if bestElements['C'] is not None:
                bestElements = bestElements['C']
            elif bestElements['A'] is not None:
                bestElements = bestElements['A']
            else:
                # no solution
                return None
        elif leftMostMin == 2:
            # C
            if bestElements['T'] is not None:
                bestElements = bestElements['T']
            elif bestElements['A'] is not None:
                bestElements = bestElements['A']
            else:
                # no solution
                return None
        else:
            # A or C+T
            if bestElements['G'] is not None:
                bestElements = bestElements['G']
            elif bestElements['C'] is not None:
                if bestElements['T'] is not None:
                    bestElements = bestElements['C'] + bestElements['T']
                else:
                    bestElements = bestElements['C']
            elif bestElements['A'] is not None:
                bestElements = bestElements['A']
            else:
                # no solution
                return None
        
        return bestElements
    

    def _score_indecies(self, indecies, raw, row_scores):
        scoring = {
            0: {
                'C': 4,
                'T': 4,
                'G': -4,
                'A': 8
            },

            1: {
                'C': 8,
                'T': -1,
                'G': -1,
                'A': 6
            },

            2: {
                'C': -1,
                'T': 8,
                'G': -1,
                'A': 6
            },

            3: {
                'C': -1,
                'T': -1,
                'G': 1,
                'A': -1
            }
        }

        # <3

        scores = []
        for i in indecies:
            score = 0
            for k, e in enumerate(raw[i]):
                score += scoring[row_scores[k]][e]
            scores.append(score)
        return scores


    def _heuristic(self, left, groups=[]):
        curr = groups[-1]
        res = None

        # Pick the leftmost minimum
        left_most_min = min(self.row_scores)
        index = self.row_scores.index(left_most_min)
        i7s = self._get_best_elements(left_most_min, index, self.i7)
        # TODO: Might be None
        i7scores = self._score_indecies(i7s, self.content['i7'], self.row_scores)
        i7zipped = list(zip(i7s, i7scores))
        
        print(self.row_scores)
        for z in i7zipped:
            print(self.content['i7'][z[0]], z[1])
        
        if self.i5 is not None:
            i5s = self._get_best_elements(leftMostMin, index, self.i5)
            # TODO: Might be None
            i5scores = self._score_indecies(i5s, self.content['i5'], self.row_scores)
            print(i5s)
        
        # Pick available indecies from 'left'

        for i in range(len(left)):
            new_left = left[:]
            del new_left[i]
            new_groups = groups[:-1] + [curr + [left[i]]]
            res = self._group(new_left, new_groups)

            if res is not None:
                groups = new_groups
                break
        
        return res


    def _heuristic_old(self, left, groups=[]):
        # Initialize row scores
        row_scores = [0 for _ in range(self.i7_len + self.i5_len)]

        for i in range(self.samples):
            # Pick the leftmost minimum
            leftMostMin = min(row_scores)
            index = row_scores.index(leftMostMin)
            i7s = self._get_best_elements(leftMostMin, index, self.i7)
            # TODO: Might be None
            i7scores = self._score_indecies(i7s, self.content['i7'], row_scores)
            i7zipped = list(zip(i7s, i7scores))
            
            print(row_scores)
            for z in i7zipped:
                print(self.content['i7'][z[0]], z[1])

            if self.i5 is not None:
                i5s = self._get_best_elements(leftMostMin, index, self.i5)
                # TODO: Might be None
                i5scores = self._score_indecies(i5s, self.content['i5'], row_scores)
                print(i5s)

            break

        return None