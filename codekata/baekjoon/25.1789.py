s = int(input())
i = 0
mysum = 0

while True:
    i += 1
    mysum += i
    if mysum > s:
        break
print(i-1)