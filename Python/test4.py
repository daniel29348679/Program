# %%
x = [0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0]
z = [0, 0, 0, 0, 0]
s = [0, 0, 0, 0, 0, 0]
mi = 100000000
sum = 0


def dfs():
    global x, y, z, s, mi, sum

    if sum > mi:
        return
    good = 1
    if x[1] + s[1] < 1:
        x[1] += 1
        sum += 120
        dfs()
        x[1] -= 1
        sum -= 120

        s[1] += 1
        sum += 150
        dfs()
        s[1] -= 1
        sum -= 150

        good = 0
    if x[3] + s[3] < 1:
        x[3] += 1
        sum += 110
        dfs()
        x[3] -= 1
        sum -= 110

        s[3] += 1
        sum += 140
        dfs()
        s[3] -= 1
        sum -= 140
        good = 0

    if x[4] + s[4] * 2 + s[5] * 4 < 3:
        x[4] += 1
        sum += 60
        dfs()
        x[4] -= 1
        sum -= 60

        s[4] += 1
        sum += 150
        dfs()
        s[4] -= 1
        sum -= 150

        s[5] += 1
        sum += 200
        dfs()
        s[5] -= 1
        sum -= 200

        good = 0

    if y[1] + s[1] + s[5] * 3 < 5:
        y[1] += 1
        sum += 55
        dfs()
        y[1] -= 1
        sum -= 55

        s[1] += 1
        sum += 150
        dfs()
        s[1] -= 1
        sum -= 150

        s[5] += 1
        sum += 200
        dfs()
        s[5] -= 1
        sum -= 200

        good = 0

    if y[2] + s[2] < 1:
        y[2] += 1
        sum += 60
        dfs()
        y[2] -= 1
        sum -= 60

        s[2] += 1
        sum += 130
        dfs()
        s[2] -= 1
        sum -= 130

        good = 0

    if y[3] + s[3] < 4:
        y[3] += 1
        sum += 45
        dfs()
        y[3] -= 1
        sum -= 45

        s[3] += 1
        sum += 140
        dfs()
        s[3] -= 1
        sum -= 140

        good = 0

    if y[4] + s[4] + s[5] * 3 < 2:
        y[4] += 1
        sum += 50
        dfs()
        y[4] -= 1
        sum -= 50

        s[4] += 1
        sum += 150
        dfs()
        s[4] -= 1
        sum -= 150

        s[5] += 1
        sum += 200
        dfs()
        s[5] -= 1
        sum -= 200

        good = 0

    if z[1] + s[1] + s[5] * 4 < 2:
        z[1] += 1
        sum += 30
        dfs()
        z[1] -= 1
        sum -= 30

        s[1] += 1
        sum += 150
        dfs()
        s[1] -= 1
        sum -= 150

        s[5] += 1
        sum += 200
        dfs()
        s[5] -= 1
        sum -= 200

        good = 0

    if z[2] + s[2] < 2:
        z[2] += 1
        sum += 30
        dfs()
        z[2] -= 1
        sum -= 30

        s[2] += 1
        sum += 130
        dfs()
        s[2] -= 1
        sum -= 130

        good = 0

    if z[3] + s[3] < 1:
        z[3] += 1
        sum += 25
        dfs()
        z[3] -= 1
        sum -= 25

        s[3] += 1
        sum += 140
        dfs()
        s[3] -= 1
        sum -= 140
        good = 0

    if x[1] + x[2] + x[3] + s[1] + s[2] + s[3] < 4:
        x[1] += 1
        sum += 120
        dfs()
        x[1] -= 1
        sum -= 120

        x[2] += 1
        sum += 100
        dfs()
        x[2] -= 1
        sum -= 100

        x[3] += 1
        sum += 110
        dfs()
        x[3] -= 1
        sum -= 110

        s[1] += 1
        sum += 150
        dfs()
        s[1] -= 1
        sum -= 150
        s[2] += 1
        sum += 130
        dfs()
        s[2] -= 1
        sum -= 130
        s[3] += 1
        sum += 140
        dfs()
        s[3] -= 1
        sum -= 140
        good = 0

    if good:
        if sum < mi:
            mi = sum
            print(x, y, z, s, sum)


dfs()
print(mi)
