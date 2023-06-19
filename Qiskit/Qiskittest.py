#%%
import numpy as np
from qiskit import *
import pylatexenc
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
from math import pi

#%%
from qiskit import IBMQ

provider = IBMQ.load_account()
backend = provider.get_backend("ibmq_qasm_simulator")

#%%
def getinitialstate(x, y):
    return [
        x / math.sqrt(abs(x) ** 2 + abs(y) ** 2),
        y / math.sqrt(abs(x) ** 2 + abs(y) ** 2),
    ]


#%%
circ = QuantumCircuit(5, 2)
circ.h([0, 3, 4])
circ.cx(0, 1)
circ.cx(1, 2)
circ.barrier()
circ.mcz([0, 1], 3)
circ.mcz([1, 2], 4)
circ.h([3, 4])
circ.measure([3, 4], [0, 1])
circ.draw("mpl")

#%%
job = backend.run(circ)
result = job.result()
counts = result.get_counts(circ)
# print(counts)
for key in counts.keys():
    print(f"'{key}' {counts[key]/4000}")
# %%
