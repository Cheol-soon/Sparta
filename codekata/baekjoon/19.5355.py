n = int(input())
for i in range(0, n):
    x = input().split()
    y = 0
    for element in x:
        if element == '@':
            y *= 3
        elif element == '%':
            y += 5
        elif element == '#':
            y -= 7
        else:
            y = float(element)
    print('%0.2f' % y)
