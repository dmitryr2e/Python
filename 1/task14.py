n, a = map(int, input().split())

res = []
cur = a
while len(res) < n:
    if cur % 2 != 0 and cur % 3 != 0 and cur % 5 != 0 and cur % 7 != 0:
        res.append(cur)
    cur += 1

print(*res)
