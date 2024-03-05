t = int(input())
for _ in range(t):
    n, l = list(map(int, input().split()))

    sets = {}
    t = []
    k = []
    for i in range(n):
        ts, ks = map(int, input().split())
        t.append(ts)
        k.append(ks)
    print(t)
    print(k)
