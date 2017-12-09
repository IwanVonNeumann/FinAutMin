def generate_protocol(trans, output, input_sequence, q_start):
    q = q_start
    protocol = []
    for a in input_sequence:
        protocol.append((a, q, output[q][a]))
        q = trans[q][a]
    return protocol
