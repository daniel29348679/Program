# %%
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from multiprocessing import Pool


class boolcirc:
    def __init__(self, qubit, errorrate):
        # self.qubit = np.array([False] * qubit, dtype=np.bool_)
        self.qubit = [False] * qubit
        self.prob = errorrate

    def checkerror(self, i, rate):
        if np.random.rand() < self.prob * rate:
            self.qubit[i] = not self.qubit[i]

    def checkerror_both(self, i, j, rate):
        if np.random.rand() < self.prob * rate:
            self.qubit[i] = not self.qubit[i]
            self.qubit[j] = not self.qubit[j]

    def checkerror_ecr(self, i, j):
        self.checkerror(i, 0.25)
        self.checkerror(j, 0.25)
        self.checkerror_both(i, j, 0.25)

    def reset(self, a):
        self.qubit[a] = False

    def x(self, a):
        self.qubit[a] = not self.qubit[a]

    def cx(self, a, b):
        if self.qubit[a]:
            self.qubit[b] = not self.qubit[b]
        self.checkerror_ecr(a, b)

    def ccx(self, c1, c2, t):
        beginstate = self.qubit[c1] ^ self.qubit[c2]

        self.checkerror_ecr(c1, t)
        self.checkerror_ecr(c2, t)
        self.checkerror_ecr(c1, t)
        self.checkerror_ecr(c2, t)

        if self.qubit[c1] and self.qubit[c2]:
            self.qubit[t] = not self.qubit[t]

        self.qubit[t] ^= beginstate ^ self.qubit[c1] ^ self.qubit[c2]

    def swap(self, a, b):
        self.cx(a, b)
        self.cx(b, a)
        self.cx(a, b)

    def swap_direct(self, a, b):
        self.qubit[a], self.qubit[b] = self.qubit[b], self.qubit[a]

    def permutation(self, a, b):
        self.qubit[a:b] = np.random.permutation(self.qubit[a:b])

    def count(self, f, e, value):
        count = 0
        for i in range(f, e):
            if self.qubit[i] == value:
                count += 1
        return count

    def __str__(self):
        s = ""
        for i in self.qubit:
            if i:
                s += "1"
            else:
                s += "0"
        return s


# %% Make a circuit
def fulladder(circuit, in1, in2, in3, carry):
    """in1, in2, in3 are the input qubits, carry is the output qubit,!!no sum"""
    circuit.ccx(in1, in2, carry)
    circuit.cx(in1, in2)
    circuit.ccx(in2, in3, carry)
    circuit.cx(in1, in2)


def testcircle(numofqubit, totaltime, coorrate, makeerror, measurerate):
    counts = [shots % numofqubit] * (totaltime // measurerate + 1)
    for _ in tqdm(range(shots // numofqubit)):
        circ = boolcirc(numofqubit + 1, prob_2)
        for k in range(totaltime + 1):
            if makeerror > 0:
                for i in range(numofqubit):
                    circ.checkerror(i, makeerror)
            if k % coorrate == coorrate - 1:
                for i in range(numofqubit):
                    fulladder(
                        circ, (i - 1) % numofqubit, i, (i + 1) % numofqubit, numofqubit
                    )
                    circ.reset(i)
                    circ.cx(numofqubit, i)
                    circ.reset(numofqubit)
            if k % measurerate == 0:
                counts[k // measurerate] += circ.count(0, numofqubit, False)
    return [i / shots for i in counts]


def testcircle_rand(numofqubit, totaltime, coorrate, makeerror, measurerate):
    counts = [shots % numofqubit] * (totaltime // measurerate + 1)
    for _ in tqdm(range(shots // numofqubit)):
        circ = boolcirc(numofqubit + 1, prob_2)
        count = 0
        for k in range(totaltime + 1):
            if makeerror > 0:
                for i in range(numofqubit):
                    circ.checkerror(i, makeerror)
            if k % coorrate == coorrate - 1:
                for i in range(numofqubit):
                    fulladder(
                        circ,
                        (i - 1 - count % 2) % numofqubit,
                        i,
                        (i + 1 + (count + 1) % 2) % numofqubit,
                        numofqubit,
                    )
                    circ.reset(i)
                    circ.cx(numofqubit, i)
                    circ.reset(numofqubit)
                for i in range(0, numofqubit, 2):
                    circ.swap(i, (i + 1) % numofqubit)
                for i in range(1, numofqubit, 2):
                    circ.swap(i, (i + 1) % numofqubit)
            if k % measurerate == 0:
                counts[k // measurerate] += circ.count(0, numofqubit, False)
    return [i / shots for i in counts]


def testcircle_r_d(numofqubit, totaltime, coorrate, makeerror, measurerate):
    counts = [shots % numofqubit] * (totaltime // measurerate + 1)
    for _ in tqdm(range(shots // numofqubit)):
        circ = boolcirc(numofqubit * 2, prob_2)
        count = 0
        for k in range(totaltime + 1):
            if makeerror > 0:
                for i in range(numofqubit):
                    circ.checkerror(i, makeerror)
            if k % coorrate == coorrate - 1:
                for i in range(numofqubit):
                    circ.reset(i + numofqubit)
                    fulladder(
                        circ,
                        (i - 1 - count % 2) % numofqubit,
                        i,
                        (i + 1 + (count + 1) % 2) % numofqubit,
                        i + numofqubit,
                    )
                for i in range(0, numofqubit, 2):
                    circ.swap(i, (i + 1) % numofqubit)
                for i in range(1, numofqubit, 2):
                    circ.swap(i, (i + 1) % numofqubit)
            for i in range(numofqubit):
                circ.swap_direct(i + numofqubit, i)
            if k % measurerate == 0:
                counts[k // measurerate] += circ.count(0, numofqubit, False)
    return [i / shots for i in counts]


def testcircle_d_p(numofqubit, totaltime, coorrate, makeerror, measurerate):
    counts = [shots % numofqubit] * (totaltime // measurerate + 1)
    for _ in tqdm(range(shots // numofqubit)):
        circ = boolcirc(numofqubit * 2, prob_2)
        count = 0
        for k in range(totaltime + 1):
            if makeerror > 0:
                for i in range(numofqubit):
                    circ.checkerror(i, makeerror)
            if k % coorrate == coorrate - 1:
                for i in range(numofqubit):
                    circ.reset(i + numofqubit)
                    fulladder(
                        circ,
                        (i - 1) % numofqubit,
                        i,
                        (i + 1) % numofqubit,
                        i + numofqubit,
                    )
            for i in range(numofqubit):
                circ.swap_direct(i + numofqubit, i)
            circ.permutation(0, numofqubit)
            if k % measurerate == 0:
                counts[k // measurerate] += circ.count(0, numofqubit, False)
    return [i / shots for i in counts]


# %%
fig = plt.figure()
fig.set_size_inches(16, 9)

prob_2 = 0.002795  # 2-qubit gate 0.007395
shots = 10000
corrrate = 1  # 200
measurerate = 5  # 200
makeerror = 20
totaltime = 100  # 2000
x = range(0, totaltime + 1, measurerate)

allsim = {}

allsim["10bit_rand"] = testcircle_rand(10, totaltime, corrrate, makeerror, measurerate)
allsim["20bit_rand"] = testcircle_rand(20, totaltime, corrrate, makeerror, measurerate)
allsim["10bit_rand_d"] = testcircle_r_d(10, totaltime, corrrate, makeerror, measurerate)
allsim["20bit_rand_d"] = testcircle_r_d(20, totaltime, corrrate, makeerror, measurerate)
allsim["10bit_d_p"] = testcircle_d_p(10, totaltime, corrrate, makeerror, measurerate)
allsim["20bit_d_p"] = testcircle_d_p(20, totaltime, corrrate, makeerror, measurerate)
allsim["40bit_d_p"] = testcircle_d_p(40, totaltime, corrrate, makeerror, measurerate)


allsim["base"] = testcircle(6, totaltime, corrrate, makeerror, measurerate)

# %%
fig = plt.figure()
fig.set_size_inches(16, 9)
plt.plot(x, allsim["10bit_rand"], color="c", label="10 r")
plt.plot(x, allsim["20bit_rand"], color="c", label="20 r")
plt.plot(x, allsim["10bit_rand_d"], color="m", label="10 rd")
plt.plot(x, allsim["20bit_rand_d"], color="m", label="20 rd")
plt.plot(x, allsim["10bit_d_p"], color="gray", label="10 dp")
plt.plot(x, allsim["20bit_d_p"], color="gray", label="20 dp")
plt.plot(x, allsim["40bit_d_p"], color="gray", label="40 dp")
plt.plot(x, allsim["base"], color="g", label="no corr")


plt.title(f"correct per {makeerror} x gates prob_2={prob_2}")  # title
plt.ylabel("correct rate")  # y label
plt.xlabel(f"{makeerror}x CX gates")  # x label
plt.legend()  # show legend

# %%
