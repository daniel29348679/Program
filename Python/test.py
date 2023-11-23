# %%
arr = [i for i in range(30)]

success0 = []
success1 = []
success2 = []
successgroup = []


def pri():
    return
    print()
    print(
        f"{arr[0]:2} {arr[1]:2} {arr[2]:2} {arr[3]:2} {arr[4]:2} {arr[5]:2} {arr[6]:2} {arr[7]:2} {arr[8]:2} {arr[9]:2} {arr[10]:2} {arr[11]:2} {arr[12]:2}"
    )
    print(f"{arr[27]:2}          {arr[28]:2}          {arr[29]:2}          {arr[13]:2}")
    print(
        f"{arr[26]:2} {arr[25]:2} {arr[24]:2} {arr[23]:2} {arr[22]:2} {arr[21]:2} {arr[20]:2} {arr[19]:2} {arr[18]:2} {arr[17]:2} {arr[16]:2} {arr[15]:2} {arr[14]:2}"
    )


for i in range(10):
    pri()
    vec = [arr[15], arr[16], arr[17]]
    vec.sort()
    successgroup.append(tuple(vec))
    vec = [arr[19], arr[20], arr[21]]
    vec.sort()
    successgroup.append(tuple(vec))
    vec = [arr[23], arr[24], arr[25]]
    vec.sort()
    successgroup.append(tuple(vec))
    success0.append(arr[15])
    success0.append(arr[16])
    success0.append(arr[17])

    success1.append(arr[19])
    success1.append(arr[20])
    success1.append(arr[21])

    success2.append(arr[23])
    success2.append(arr[24])
    success2.append(arr[25])
    for j in range(0, 28, 2):
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    pri()
    arr[28], arr[22] = arr[22], arr[28]
    arr[29], arr[8] = arr[8], arr[29]
    pri()
    for j in range(1, 28, 2):
        arr[j], arr[(j + 1) % 28] = arr[(j + 1) % 28], arr[j]
    pri()
    arr[28], arr[22] = arr[22], arr[28]
    arr[29], arr[8] = arr[8], arr[29]

success = success0 + success1 + success2
success.sort()
print(len(success))
print(success)
print(success1)
successgroup.sort()
print(successgroup)
