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


# %%
circ = QuantumCircuit(9)
circ.cx(0, [3, 6])
circ.barrier()
circ.h([0, 3, 6])
circ.cx(0, [1, 2])
circ.cx(3, [4, 5])
circ.cx(6, [7, 8])
circ.barrier()
# error here
circ.z([1, 2, 3, 4, 5, 6, 7, 8])
circ.barrier()
circ.cx(0, [1, 2])
circ.cx(3, [4, 5])
circ.cx(6, [7, 8])
circ.ccx(2, 1, 0)
circ.ccx(5, 4, 3)
circ.ccx(8, 7, 6)

circ.h([0, 3, 6])
circ.cx(0, [3, 6])
circ.ccx(6, 3, 0)

circ.measure_all()
circ.draw("mpl")
# %%
circ = transpile(circ, simulator)

result = simulator.run(circ).result()
counts = result.get_counts(circ)
plot_histogram(counts, title="")
# %%
