#%%
from qiskit import IBMQ

provider = IBMQ.save_account(
    "39d838ca78cb7a0874c70f40dd6f4a9b81a81e78b4263873e1ed73ed96f0f9016a57a701f3c6ada6d837f27a5232bd83f2522f6eab20ba363a38b74b68a814a3",
    overwrite=True,
)
#%%
provider = IBMQ.load_account()
backend = provider.get_backend("ibmq_qasm_simulator")
IBMQ.disable_account()

# %%
