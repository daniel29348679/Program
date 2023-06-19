# %%
import numpy as np
from qiskit import *
import pylatexenc
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
from math import pi
from qiskit.tools.visualization import plot_histogram, plot_state_city
from qiskit.circuit.library import SurfaceCode

simulator = Aer.get_backend("aer_simulator")


# %%
code = SurfaceCode(5, 5)
circ = QuantumCircuit(code)


circ.draw("mpl")

# %%
circ = transpile(circ, simulator)

result = simulator.run(circ).result()
counts = result.get_counts(circ)
plot_histogram(counts, title="")
# %%
