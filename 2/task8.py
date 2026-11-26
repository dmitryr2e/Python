import math

x, y = map(float, input().split())

ans = math.floor(y) - math.ceil(x) + 1
if ans < 0:
    ans = 0

print(ans)
