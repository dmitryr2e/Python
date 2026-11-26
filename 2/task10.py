s = input()

res = ""
for char in s[::-1]:
    if char == "(":
        res += ")"
    else:
        res += "("

print(res)
