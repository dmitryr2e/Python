n = int(input())

cnt = 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        cnt += i
        if i != n // i:
            cnt += n // i

print(cnt)
