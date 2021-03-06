from equality import equality_classes
from minimization import new_states_map, new_output_rules, new_transition_rules
from protocol import generate_protocol


def solve_minimization(A, Q, niu, zeta):
    C = equality_classes(A, Q, niu, zeta)
    Q_map = new_states_map(C)
    zeta_ = new_output_rules(A, Q_map, zeta)
    niu_ = new_transition_rules(A, Q_map, niu)

    print("Equality classes:")
    print(C)
    print()

    print("New states map:")
    print(Q_map)
    print()

    print("New output function:")
    for x in zeta_:
        print(x, zeta_[x])
    print()

    print("New transition function:")
    for x in niu_:
        print(x, niu_[x])
    print()


def solve_protocol(niu, zeta, input_sequence, q_start):
    protocol = generate_protocol(niu, zeta, input_sequence, q_start)

    print("Protocol:")
    for line in protocol:
        print(line)
    print()
