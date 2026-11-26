n = int(input())
nums = list(map(int, input().split()))

res = []
for x in nums:
    bx = bin(x)[2:]
    by = bin(len(bx))[2:]
    z = len(by)
    res.append("0" * (z - 1) + by + bx[1:])

print("".join(res))
