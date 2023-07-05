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
code_h = 8
code_w = 5
morequbit = 1
bit = 5
circ = QuantumCircuit(code_h * code_w + morequbit, bit)


def lti(x, y):
    """2D locate to index"""
    return x + y * code_w


def stabilizer_z(x, y):
    """Z stabilizer"""
    if 0 <= x + 1 and x + 1 < code_w and 0 <= y and y < code_h:
        circ.cx(lti(x + 1, y), lti(x, y))
    if 0 <= x - 1 and x - 1 < code_w and 0 <= y and y < code_h:
        circ.cx(lti(x - 1, y), lti(x, y))
    if 0 <= x and x < code_w and 0 <= y + 1 and y + 1 < code_h:
        circ.cx(lti(x, y + 1), lti(x, y))
    if 0 <= x and x < code_w and 0 <= y - 1 and y - 1 < code_h:
        circ.cx(lti(x, y - 1), lti(x, y))


def stabilizer_x(x, y):
    """X stabilizer"""
    circ.h(lti(x, y))
    if 0 <= x + 1 and x + 1 < code_w and 0 <= y and y < code_h:
        circ.cx(lti(x, y), lti(x + 1, y))
    if 0 <= x - 1 and x - 1 < code_w and 0 <= y and y < code_h:
        circ.cx(lti(x, y), lti(x - 1, y))
    if 0 <= x and x < code_w and 0 <= y + 1 and y + 1 < code_h:
        circ.cx(lti(x, y), lti(x, y + 1))
    if 0 <= x and x < code_w and 0 <= y - 1 and y - 1 < code_h:
        circ.cx(lti(x, y), lti(x, y - 1))
    circ.h(lti(x, y))


stabilizer_x_list = []
stabilizer_z_list = []


def stabilize():
    """Do stabilize"""
    for i in stabilizer_x_list:
        stabilizer_x(i[0], i[1])
    for i in stabilizer_z_list:
        stabilizer_z(i[0], i[1])


def init_state():
    """Initialize state"""
    for i in range(1, code_w, 2):
        for j in range(0, code_h, 2):
            stabilizer_x_list.append((i, j))

    for i in range(0, code_w, 2):
        for j in range(1, code_h, 2):
            stabilizer_z_list.append((i, j))


def hole_z(x, y):
    """Z hole Qubit"""
    stabilizer_z_list.remove((x, y))


init_state()
hole_z(2, 5)
stabilize()
circ.x([lti(2, 0), lti(2, 2)])
stabilize()

circ.measure(lti(2, 3), 4)
circ.measure([lti(1, 5), lti(3, 5), lti(2, 4), lti(2, 6)], [0, 1, 2, 3])

# circ.draw("mpl")
circ = transpile(circ, simulator)

result = simulator.run(circ).result()
counts = result.get_counts(circ)
plot_histogram(counts, title="")
# %%
