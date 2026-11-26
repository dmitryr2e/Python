words = input().split()

res = []
for word in words:
    res.append(word[::-1])

print(*res)
