#%%
import numpy as np
from qiskit import *
import pylatexenc
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
from math import *

#%%
def getinitialstate(x, y):
    return [
        x / sqrt(abs(x) ** 2 + abs(y) ** 2),
        y / sqrt(abs(x) ** 2 + abs(y) ** 2),
    ]


circ = QuantumCircuit(3)
circ.h([0, 1, 2])
for i in range(1):
    circ.barrier()
    circ.x(0)
    circ.mcp(pi, [0, 1], 2)
    circ.x(0)

    circ.barrier()

    circ.h([0, 1, 2])
    circ.x([0, 1, 2])
    circ.mcp(pi, [0, 1], 2)
    circ.x([0, 1, 2])
    circ.h([0, 1, 2])
circ.draw("mpl")
# %%
backend = Aer.get_backend("statevector_simulator")
job = backend.run(circ)
result = job.result()
counts = result.get_counts(circ)
print(counts)
# %%
state = Statevector.from_int(0, 2**3)
state = state.evolve(circ)
state.draw("latex")
#%%
array_to_latex(state)
#%%
state.draw("qsphere")

# %%
