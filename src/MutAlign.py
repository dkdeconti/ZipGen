#!/usr/bin/python

import NTTools
import random

class MutAlignDFS():
    def __init__(self):
        pass

    def last_dfs(self, a, previous, scores, is_shift_two):
        best_score, best_matches = 0, []
        if is_shift_two:
            cur_shift_idx = 2
        else:
            cur_shift_idx = 3
        for mutant, match_score in scores[previous].items():
            best_score, best_matches = update_best(match_score,
                                                   (previous, mutant),
                                                   best_score,
                                                   best_matches)
        # ToDo fix the final choice in if statement
        if a in [match[cur_shift_idx:] for match in best_matches]:
            best_match = a
        else:
            best_match = random.choice(best_matches)[0]
        return best_score, best_match


    def limited_dfs(self, a, b, scores, is_shift_two, previous=None, limit=3):
        if limit > 0: print(limit)
        best_score, best_matches = 0, []
        if is_shift_two:
            cur_shift_idx, alt_shift_idx = 2, 3
        else:
            cur_shift_idx, alt_shift_idx = 3, 2
        for current in scores:
            if previous and previous[alt_shift_idx:] != current[alt_shift_idx:]:
                continue
            for mutant in scores[current]:
                match_score = scores[current][mutant]
                next_best = 0
                if (len(a) > 1 and len(b) > 1) and limit > 0:
                    altered_b = [mutant] + b[1:]
                    next_best, next_choice = self.limited_dfs(altered_b,
                                                              a[1:],
                                                              scores,
                                                              not is_shift_two,
                                                              previous=current,
                                                              limit=limit-1)
                best_score, best_matches = self.update_best(match_score + next_best,
                                                            (current, mutant),
                                                            best_score,
                                                            best_matches)
        if a[0] in [match[0] for match in best_matches]:
            best_match = a[0]
        else:
            best_match = random.choice(best_matches)[0]
        return best_score, best_match


    def align(self, a, b, scores, is_shift_two):
        tracker = True
        a_build, b_build = [], []
        previous = None
        match = a[0]
        while len(a) > 0 and len(b) > 0:
            _, match = self.limited_dfs(a,
                                        b,
                                        scores,
                                        is_shift_two,
                                        previous=previous)
            a.pop(0) # ToDo check if deque improves performance
            previous = match
            a_build.append(match)
            a, b = b, a
            a_build, b_build = b_build, a_build
            tracker = not tracker
            is_shift_two = not is_shift_two
        _, match = self.last_dfs(a[0], match, scores)
        a_build.append(match)
        if not tracker:
            a_build, b_build = b_build, a_build
        return a_build, b_build


    def update_best(self, score, match, best_score, best_match):
        if score > best_score:
            best_match = [match]
            best_score = score
        elif score == best_score:
            best_match.append(match)
        return best_score, best_match


class MutAlignGreedy():
    def __init__(self):
        self.codons = NTTools.get_codons()


    def align(self, a, b, scores, is_shift_two):
        tracker = True
        a_build, b_build = [], []
        previous = None
        while len(a) > 0 and len(b) > 0:
            if previous:
                _, match = self.greedy_mut(a, 
                                           scores, 
                                           is_shift_two, 
                                           previous=previous)
            else:
                match = a[0]
            a_build.append(match)
            previous = a.pop(0)
            is_shift_two = not is_shift_two
            a, b = b, a
            a_build, b_build = b_build, a_build
            tracker = not tracker
        if not tracker:
            a_build, b_build = b_build, a_build
        return a_build, b_build
            

    def filter_codon_by_previous(self, previous, is_shift_two):
        if is_shift_two:
            shift_index = 2
        else:
            shift_index = 3
        filter_set = set([])
        for codon in self.codons:
            if codon[:shift_index+1] == previous[:shift_index+1]:
                filter_set.add(codon)
        return filter_set


    def greedy_mut(self, a, scores, is_shift_two, previous=None):
        skip_codons = self.filter_codon_by_previous(previous, is_shift_two)
        best_match, best_score = [], -inf
        for codon in self.codons:
            if codon not in skip_codons:
                score = scores[a][codon]
                self.update_best(codon, score, best_match, best_score)
        if a in best_match:
            best_match = a
        else:
            best_match = random.choice(best_match)
        return best_score, best_match


    def update_best(self, codon, score, best_match, best_score):
        if score > best_score:
            best_score = score
            best_match = [codon]
        elif score == best_score:
            best_match.append(codon)
        return best_match, best_score
