s = input()

res = []
idx = 0
while idx < len(s):
    zeros = 0
    while s[idx] == "0":
        zeros += 1
        idx += 1
    z = zeros + 1
    y = int(s[idx : idx + z], 2)
    idx += z
    x = int("1" + s[idx : idx + y - 1], 2)
    idx += y - 1
    res.append(x)

print(len(res))
print(*res)
