t = int(input())

res = []
for i in range(t):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    left = (a1 * b2 + a2 * b1) * b3 * b4
    right = (a3 * b4 + a4 * b3) * b1 * b2
    if left < right:
        res.append(-1)
    elif left > right:
        res.append(1)
    else:
        res.append(0)

print(*res)
