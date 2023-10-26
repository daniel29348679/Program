# %%
import numpy as np
from qiskit import *
import pylatexenc
from qiskit.quantum_info import Statevector
from qiskit.quantum_info.operators import Operator, Pauli
from qiskit.visualization import *
from math import *
from qiskit.extensions import RXGate, XGate, CXGate


def getinitialstate(x, y):
    return [
        x / sqrt(abs(x) ** 2 + abs(y) ** 2),
        y / sqrt(abs(x) ** 2 + abs(y) ** 2),
    ]


# %%
circ = QuantumCircuit(1)
circ.x(0)
circ.ry(0.1, 0)
circ.draw("mpl")
# %%
backend = Aer.get_backend("statevector_simulator")
job = backend.run(circ)
result = job.result()
outputstate = result.get_statevector(circ)
plot_bloch_multivector(outputstate, reverse_bits=True)

# %%
