from itertools import permutations

import algorithmChecker as ac
import random


class Algorithm:
    def __init__(self, runs, samples, content, i7, i5=None):
        if 'i5' not in content:
            self.indecies = [(i, ) for i in range(len(content['i7']))]
        else:
            self.indecies = [(i, j) for i in range(len(content['i7'])) for j in range(len(content['i5']))]
        
        self.i7 = i7
        self.i5 = i5
        self.content = content
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
            txt = self.content['i7'][sample[0]]
            if self.i5 is not None:
                txt += self.content['i5'][sample[1]]
            converted.append(txt)
        
        return ac.checkAlgorithm(converted)
    

class QuadChannel(Algorithm):
    def _checkGroup(self, group):
        converted = []

        for sample in group:
            txt = self.content['i7'][sample[0]]
            if self.i5 is not None:
                txt += self.content['i5'][sample[1]]
            converted.append(txt)
        
        return ac.checkAlgorithm_4Channel(converted)


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


class QuadForce(QuadChannel):
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
        super().__init__(runs, samples, content, i7, i5)

        self.test123 = None
        self.i7_len = len(content['i7'][0])
        self.i5_len = len(content['i5'][0]) if 'i5' in content else 0

    
    def _new_group_extra(self):
        self.row_scores = [0 for _ in range(self.i7_len + self.i5_len)]
    
    
    def _get_best_elements(self, leftMostMin, index, structure):
        # print(structure)
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


    def _calc_index_score(self, sample):
        txt = self.content['i7'][sample[0]]
        if self.i5 is not None:
            txt += self.content['i5'][sample[1]]
        
        enzyme_scores = {
            'A': 0b11,
            'C': 0b10,
            'T': 0b01,
            'G': 0b00
        }

        scores = [0 for _ in range(len(txt))]
        for i, c in enumerate(txt):
            scores[i] = enzyme_scores[c]

        return scores


    def _heuristic(self, left, groups=[]):
        curr = groups[-1]
        res = None

        if 'i5' in self.content and len(curr) == 0 and len(groups) > 1:
            permutable = groups[-2]

            x = [a[0] for a in permutable]
            y = [a[1] for a in permutable]
            perm = list(set(permutations(y)))

            perm_groups = []
            for p in perm:
                candidate = list(set(list(zip(x, p))).intersection(set(left)))
                if len(candidate) == self.samples:
                    perm_groups.append(candidate)
                    for c in candidate:
                        left.remove(c)


            del groups[-1]
            for pg in perm_groups:
                if len(groups) >= self.samples:
                    break
                
                groups.append(pg)
            
            if len(groups) < self.samples:
                groups.append([])
            else:
                return groups

        if len(curr) == 0:
            tmp_row_scores = self.row_scores[:]

            a = random.choice(left)
            new_left = left[:]
            new_left.remove(a)

            # Calculate new row scores
            new_scores = self._calc_index_score(a)
            # print(self.row_scores, "+", new_scores, "=", end=" ")
            self.row_scores = [self.row_scores[i] | new_scores[i] for i in range(len(self.row_scores))]
            # print(self.row_scores)
            
            new_groups = groups[:-1] + [curr + [a]]
            res = self._group(new_left, new_groups)

            if res is not None:
                groups = new_groups
            else:
                self.row_scores = tmp_row_scores[:]
        else:
            # Pick the leftmost minimum
            left_most_min = min(self.row_scores[:self.i7_len])
            index = self.row_scores[:self.i7_len].index(left_most_min)
            i7s = self._get_best_elements(left_most_min, index, self.i7)
            
            if i7s is None:
                return None

            i7scores = self._score_indecies(i7s, self.content['i7'], self.row_scores)
            i7zipped = list(zip(i7s, i7scores))

            if self.i5 is None:
                rank = [(x[0], ) for x in sorted(i7zipped, key=lambda x: x[1], reverse=True)]
            else:
                left_most_min = min(self.row_scores[self.i7_len:])
                index = self.row_scores[self.i7_len:].index(left_most_min)
                i5s = self._get_best_elements(left_most_min, index, self.i5)
                
                if i5s is None:
                    return None

                i5scores = self._score_indecies(i5s, self.content['i5'], self.row_scores)
                i5zipped = list(zip(i5s, i5scores))
                i7i5summed = [(i[0], j[0], i[1]+j[1]) for i in i7zipped for j in i5zipped]
                rank = [(x[0], x[1]) for x in sorted(i7i5summed, key=lambda x: x[2], reverse=True)]

            # Pick available indecies from 'left'
            available = [a for a in rank if a in left]
            # print(groups)

            tmp_row_scores = self.row_scores[:]
            # print(groups)

            for a in available:
                new_left = left[:]
                new_left.remove(a)

                # Calculate new row scores
                new_scores = self._calc_index_score(a)
                # print(self.row_scores, "+", new_scores, "=", end=" ")
                self.row_scores = [self.row_scores[i] | new_scores[i] for i in range(len(self.row_scores))]
                # print(self.row_scores)
                
                new_groups = groups[:-1] + [curr + [a]]
                res = self._group(new_left, new_groups)

                if res is not None:
                    groups = new_groups
                    break
                else:
                    self.row_scores = tmp_row_scores[:]
        
        return res
