t = int(input())

for ind in range(t):

    n = int(input())
    a = [0, 0, 0, 0, 0]

    temp = n
    index = 0

    for i in range(2, n+1):

        flag = 0

        if temp % i == 0:
            flag = 1
            while temp % i == 0:
                a[index] += 1
                temp //= i

        if flag == 1:
            index += 1

    print(f"#{ind+1} {a[0]} {a[1]} {a[2]} {a[3]} {a[4]}")
