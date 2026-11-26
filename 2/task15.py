n = int(input())

ans = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        ans += a - b

print(ans)
