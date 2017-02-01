#! /usr/bin/python

import copy
import random


def align(a, b, scores):
    tracker = 0
    a_build, b_build = [], []
    previous = None
    match = a[0]
    while len(a) > 0 and len(b) > 0:
        _, match = limited_dfs(a,
                               b,
                               scores,
                               previous=previous)
        a.pop(0)
        previous = match
        a_build.append(match)
        a, b = b, a
        a_build, b_build = b_build, a_build
        tracker += 1
    _, match = last_dfs(a[0], match, scores)
    a_build.append(match)
    if tracker % 2 == 1:
        a_build, b_build = b_build, a_build
    return a_build, b_build


def last_dfs(a, previous, scores):
    print("last")
    best_score, best_matches = 0, []
    for right, match_score in scores[previous].items():
        best_score, best_matches = update_best(match_score,
                                               (previous, right),
                                               best_score,
                                               best_matches)
    if a in [match[1] for match in best_matches]:
        best_match = a
    else:
        best_match = random.choice(best_matches)[0]
    return best_score, best_match


def limited_dfs(a, b, scores, previous=None, limit=3):
    best_score, best_matches = 0, []
    for left in scores:
        if previous:
            if previous[1] != left[0]:
                continue
        for right in scores[left]:
            match_score = scores[left][right]
            next_best = 0
            if (len(a) > 1 and len(b) > 1) and limit > 0:
                altered_b = [right] + b[1:]
                next_best, next_choice = limited_dfs(altered_b,
                                                     a[1:],
                                                     scores,
                                                     previous=left,
                                                     limit=limit-1)
            best_score, best_matches = update_best(match_score + next_best,
                                                   (left, right),
                                                   best_score,
                                                   best_matches)
    if a[0] in [match[0] for match in best_matches]:
        best_match = a[0]
    else:
        best_match = random.choice(best_matches)[0]
    return best_score, best_match


def update_best(score, match, best_score, best_match):
    if score > best_score:
        best_match = [match]
        best_score = score
    elif score == best_score:
        best_match.append(match)
    return best_score, best_match


def vectorize_sequence(s):
    # ToDo change from vector to deque in collections
    return [s[i:i+2] for i in range(0, len(s), 2)]


def main():
    a = "0010100110"
    b =  "0101001101"
    c =  "0110001011"
    scores = {"00": {"00": 10,
                     "01": 10,
                     "10": 1,
                     "11": 1},
              "01": {"00": 1,
                     "01": 1,
                     "10": 10,
                     "11": 10},
              "10": {"00": 10,
                     "01": 10,
                     "10": 1,
                     "11": 1},
              "11": {"00": 1,
                     "01": 1,
                     "10": 10,
                     "11": 10}}
    print(a)
    print("", b)
    print("", c)
    #print("-----------")
    #x, y = align(vectorize_sequence(a), vectorize_sequence(b), scores)
    #print(''.join(x))
    #print("", ''.join(y))
    print("-----------")
    x, z = align(vectorize_sequence(a), vectorize_sequence(c), scores)
    print(''.join(x))
    print("", ''.join(z))


if __name__ == "__main__":
    main()
