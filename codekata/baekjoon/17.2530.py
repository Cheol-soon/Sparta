hour, minute, second = map(int, input().split())
eta = int(input())

calsec = eta % 60
calmin = int((eta % 3600 - calsec)/60)
calhour = int(eta/3600)

print(f'{int(hour + calhour + (int(minute + calmin + int((second + calsec)/60))/60)) %
      24} {int(minute + calmin + int((second + calsec)/60)) % 60} {(second + calsec) % 60}')
# print(f'{(hour + calhour + int((minute + calmin + int((second+calsec) / 60)) / 60) %24)} {(minute + calmin + int((second+calsec) / 60)) % 60} {(second+calsec) % 60}')
