# %%
# i = 2,3,4,5,6,,,,,,,100
for i in range(2, 101):
    isprime = True  # 是不是質數 先預設是質數

    # 假設 i = 9 ,j 會是 2,3,4,5,6,7,8 ,即所有可能為9的因數的數
    for j in range(2, i):
        # 如果 i 能被 j 整除，則 i 不是質數
        if i % j == 0:
            isprime = False

    # 如果 i 是質數，則印出來
    if isprime:
        print(i)
