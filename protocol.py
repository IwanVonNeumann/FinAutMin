def generate_protocol(trans, output, q_start, input_sequence):
    q = q_start
    protocol = []
    for a in input_sequence:
        protocol.append((a, q, output[q][a]))
        q = trans[q][a]
    return protocol


def print_protocol(protocol):
    for line in protocol:
        print(line)
