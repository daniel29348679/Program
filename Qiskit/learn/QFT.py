# QFT
def qft(circuit, qbits):
    for hbit in range(len(qbits) - 1, -1, -1):
        circuit.h(qbits[hbit])
        for cbit in range(hbit):
            circuit.cp(pi / 2 ** (hbit - cbit), qbits[cbit], qbits[hbit])
    for bit in range(len(qbits) // 2):
        circuit.swap(qbits[bit], qbits[len(qbits) - bit - 1])


# IQFT
def iqft(circuit, qbits):
    for bit in range(len(qbits) // 2):
        circuit.swap(qbits[bit], qbits[len(qbits) - bit - 1])
    for hbit in range(0, len(qbits), 1):
        for cbit in range(hbit):
            circuit.cp(-pi / 2 ** (hbit - cbit), qbits[cbit], qbits[hbit])
        circuit.h(qbits[hbit])
