from collections import defaultdict


def equality_classes(A, Q, trans, output):
    C = one_equality_classes(A, Q, output)
    i = 1
    print("P{} =".format(i), C)
    C_ = next_level_equality_classes(A, C, trans)
    while len(C) != len(C_):
        C = C_
        i += 1
        print("P{} =".format(i), C)
        C_ = next_level_equality_classes(A, C, trans)
    print()
    return C_


def one_equality_classes(A, Q, output):
    C = defaultdict(set)
    for q in Q:
        footprint = tuple([output[q][a] for a in A])
        C[footprint].add(q)
    return list(C.values())


def next_level_equality_classes(A, C, trans):
    C_ = []
    for c in C:
        S = defaultdict(set)
        for q in c:
            f = transitions_footprint(A, C, trans[q])
            S[f].add(q)
        C_.extend(S.values())
    return C_


# TODO simplify using hashed types
def transitions_footprint(A, C, q_trans):
    class_footprints = []
    for a in A:
        q_ = q_trans[a]
        for c in C:
            if q_ in c:
                footprint = frozenset(c)
                class_footprints.append(footprint)
    return tuple(class_footprints)
