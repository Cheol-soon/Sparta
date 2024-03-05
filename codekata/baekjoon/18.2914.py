import math

song, average = map(int, input().split())
print(song*(average-1)+1)

# melody / song = ceil(average)
