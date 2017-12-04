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


def transitions_footprint(A, C, q_trans):
    class_footprints = list()
    for a in A:
        q_ = q_trans[a]
        for c in C:
            if q_ in c:
                class_footprints.append(class_footprint(c))
    return "_".join(class_footprints)


def class_footprint(c):
    return "".join(sorted(list(c)))
