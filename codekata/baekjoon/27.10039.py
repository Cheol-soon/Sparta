S = 0
for i in range(5):
    score = int(input())

    if score <= 40:
        S += 40
    else:
        S += score

print(int(S/5))
