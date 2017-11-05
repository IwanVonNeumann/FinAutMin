def new_states_map(C):
    Q_ = {}
    i = 1
    for c in C:
        q_name = new_name(i)
        Q_[q_name] = c
        i += 1
    return Q_


def new_name(i):
    return "q{}~".format(i)


def new_output_rules(A, q_map, old_out):
    new_out = {}
    for q_new in q_map.keys():
        q_old = list(q_map[q_new])[0]
        new_out[q_new] = {a: old_out[q_old][a] for a in A}
    return new_out


def new_transition_rules(A, q_map, old_trans):
    new_trans = {}
    q_map_inv = new_states_map_inv(q_map)
    for q_new in q_map.keys():
        q_old = list(q_map[q_new])[0]
        new_trans[q_new] = {a: q_map_inv[old_trans[q_old][a]] for a in A}
    return new_trans


def new_states_map_inv(q_map):
    q_map_inv = {}
    for k in q_map.keys():
        for v in q_map[k]:
            q_map_inv[v] = k
    return q_map_inv
