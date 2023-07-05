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
circ = QuantumCircuit(10, 2)
# x => 3,5
# z => 1,7
circ.h([3, 5])
circ.cx(3, [0, 4, 6])
circ.cx(5, [2, 4, 8])

circ.cx([0, 2, 4], 1)
circ.cx([4, 6, 8], 7)

circ.cx(4, 9)
circ.x(4)

circ.cx(3, [0, 4, 6])
circ.cx(5, [2, 4, 8])

circ.cx([0, 2, 4], 1)
circ.cx([4, 6, 8], 7)

circ.measure([4, 9], [0, 1])
circ.draw("mpl")
# %%
circ = transpile(circ, simulator)

result = simulator.run(circ).result()
counts = result.get_counts(circ)
plot_histogram(counts, title="")
# %%
