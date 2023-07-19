# %%


[m, n] = [int(n) for n in input().split()]
numbers = [int(n) for n in input().split()]
arr = [0] * (m + 1)

for i in range(m):
    arr[i + 1] = arr[i] + numbers[i]

while n > 0:
    [a, b] = [int(n) for n in input().split()]
    print(arr[b] - arr[a - 1])
    n -= 1

# %%
