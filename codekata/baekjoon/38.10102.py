n = int(input())

s = input()

if s.count('A') > s.count('B'):
    print('A')
elif s.count('A') == s.count('B'):
    print('Tie')
else:
    print('B')