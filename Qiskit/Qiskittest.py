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
backend = provider.get_backend("ibm_lagos")


# %%
circ = QuantumCircuit(1, 1)

for i in range(5):
    circ.h(0)
    circ.barrier()
    circ.h(0)
    circ.barrier()

circ.measure(0, 0)
# circ.draw("mpl")
# %%
shots = 2000
job = backend.run(circ, shots=shots)
result = job.result()
counts = result.get_counts(circ)

print(counts)
# %%
