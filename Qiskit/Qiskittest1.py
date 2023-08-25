# %%
import numpy as np
from qiskit import *
import pylatexenc
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
from math import pi
from qiskit.tools.visualization import plot_histogram, plot_state_city

simulator = Aer.get_backend("aer_simulator")


# %%
def getinitialstate(x, y):
    return [
        x / math.sqrt(abs(x) ** 2 + abs(y) ** 2),
        y / math.sqrt(abs(x) ** 2 + abs(y) ** 2),
    ]


def fulladder(circuit, in1, in2, in3, carry):
    """in1, in2, in3 are the input qubits, carry is the output qubit,!!no sum"""
    circuit.ccx(in1, in2, carry)
    circuit.cx(in1, in2)
    circuit.ccx(in2, in3, carry)
    circuit.cx(in1, in2)


# %%
circ = QuantumCircuit(4)
circ.x([0])
fulladder(circ, 0, 1, 2, 3)
circ.measure_all()
circ.draw("mpl")
# %%
circ = transpile(circ, simulator)

result = simulator.run(circ).result()
counts = result.get_counts(circ)
plot_histogram(counts, title="")
# %%
