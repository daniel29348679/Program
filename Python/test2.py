#%%
import numpy as np


def swap(a, b):
    z = a
    a = b
    b = z


a = {"name": 1}
b = {"name": 2}
swap(a, b)
print(a, b)
# %%
