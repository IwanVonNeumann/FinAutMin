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
    C = {}
    for q in Q:
        f = out_footprint(A, output[q])
        if f in C:
            C[f].add(q)
        else:
            C[f] = {q}
    return list(C.values())


def out_footprint(A, q_out):
    return "".join([q_out[a] for a in A])


def next_level_equality_classes(A, C, trans):
    C_ = []
    for c in C:
        S = {}
        for q in c:
            f = transitions_footprint(A, C, trans[q])
            if f in S:
                S[f].add(q)
            else:
                S[f] = {q}
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
