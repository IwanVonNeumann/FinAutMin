from equality import equality_classes
from minimization import new_states_map, new_output_rules, new_transition_rules

A = {"a", "b"}
Z = {"0", "1"}
Q = {"q1", "q2", "q3", "q4", "q5", "q6"}

niu = {
    "q1": {"a": "q4", "b": "q3"},
    "q2": {"a": "q6", "b": "q1"},
    "q3": {"a": "q4", "b": "q1"},
    "q4": {"a": "q5", "b": "q5"},
    "q5": {"a": "q2", "b": "q6"},
    "q6": {"a": "q2", "b": "q3"}
}

zeta = {
    "q1": {"a": "1", "b": "0"},
    "q2": {"a": "0", "b": "1"},
    "q3": {"a": "1", "b": "0"},
    "q4": {"a": "1", "b": "0"},
    "q5": {"a": "1", "b": "0"},
    "q6": {"a": "0", "b": "1"}
}

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
