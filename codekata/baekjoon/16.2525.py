hour, minute = map(int, input().split())
eta = int(input())

print(f'{(hour+int(eta/60) + int((minute + (eta % 60))/60)
          ) % 24} {(minute + (eta % 60)) % 60}')
