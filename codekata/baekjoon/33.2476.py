n = int(input())

reward = []
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    if a == b and b == c:
        reward.append(10000+a*1000)
    elif a == b or b == c or a == c:
        if a == b:
            reward.append(1000+a*100)
        elif b == c:
            reward.append(1000+b*100)
        else:
            reward.append(1000+a*100)
    else:
        reward.append(max([a, b, c])*100)
print(max(reward))
