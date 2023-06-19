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

circ = QuantumCircuit(6)

circ.h(0)
circ.cx(0, [1, 2, 3])
circ.z(0)
circ.barrier()
circ.ry(-pi / 2, 4)
circ.cz([0, 1, 2, 3], 4)
circ.ry(pi / 2, 4)
circ.barrier()
circ.ry(-pi / 2, 5)
circ.ry(pi / 2, [0, 1, 2, 3])
circ.cz([0, 1, 2, 3], 5)
circ.ry(-pi / 2, [0, 1, 2, 3])
circ.ry(pi / 2, 5)
circ.measure_all()
circ.draw("mpl")

# %%
circ = transpile(circ, simulator)

result = simulator.run(circ).result()
counts = result.get_counts(circ)
plot_histogram(counts, title="")
# %%
