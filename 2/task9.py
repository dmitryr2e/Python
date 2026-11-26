s = input()

cnt = 0
for char in s:
    if char in "0123456789":
        cnt += int(char)

print(cnt)
