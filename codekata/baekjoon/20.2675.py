T = int(input())

for _ in range(T):
    S = input().split()
    for element in S[1]:
        for i in range(0, int(S[0])):
            print(element, end='')
    print('')
