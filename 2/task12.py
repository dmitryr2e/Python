nums = list(map(int, input().split()))

res = []
for num in nums:
    ans = num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            ans = i
            break
    res.append(ans)

print(*res)
