# %%
import numpy as np
from qiskit import *
import pylatexenc
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
from math import pi

# %%
from qiskit_ibm_provider import IBMProvider

provider = IBMProvider()
print(provider.backends())
backend = provider.get_backend("ibmq_qasm_simulator")


# %%
def getinitialstate(x, y):
    return [
        x / math.sqrt(abs(x) ** 2 + abs(y) ** 2),
        y / math.sqrt(abs(x) ** 2 + abs(y) ** 2),
    ]


# %%
total = 32
circ = QuantumCircuit(total)
circ.h(0)
for i in range(1, total):
    circ.cx(i - 1, i)
circ.measure_all()
circ.draw("mpl")

# %%
job = backend.run(circ)
result = job.result()
counts = result.get_counts(circ)
# print(counts)
for key in counts.keys():
    print(f"'{key}' {counts[key]/4000}")
# %%
