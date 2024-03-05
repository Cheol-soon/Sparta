s = input()

height = 0
for i in range(len(s)):
    if i == 0:
        height += 10
    else:
        if s[i-1] == s[i]:
            height += 5
        elif not s[i-1] == s[i]:
            height += 10
print(height)
