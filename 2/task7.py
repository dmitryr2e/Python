import math

data = input().split()
n = int(data[0])
t = float(data[1])

bpm = math.ceil(n * 60 / t)
print(bpm)
